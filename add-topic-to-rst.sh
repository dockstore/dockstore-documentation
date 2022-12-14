#!/bin/bash
#
#    Copyright 2022 OICR and UCSC
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

# This script determines if a specified RST references a discourse topic, and if not, it attempts to
# extract some information from the RST, create a Discourse topic, and modify the RST to reference the new topic.

set -e
set -u

source helpers.sh

DOCS_URL="https://docs.dockstore.org/en/develop"
DISCOURSE_URL="https://discuss.dockstore.org/posts.json"
DISCOURSE_CATEGORY=12

file=$1

# Check if the file exists.
if ! [ -f "$file" ]; then
    echo "${file} does not exist."
    echo "No action taken."
    exit 1
fi

# Make sure this is a file with suffix 'rst' that is referenced from the root of the repo.
if ! [[ "$file" =~ ^docs/.*\.rst$ ]]; then
    echo "${file} should have suffix 'rst' and be referenced relative to the root of the documentation repo."
    echo "Example: docs/some-category/some-documentation.rst"
    echo "No action taken."
    exit 1
fi

# Check if the file already contains a discourse topic.
if containsDiscourseTopic; then
    echo "${file} has a discourse topic."
    echo "No action taken."
    exit 1
fi

# Check if the file contains a top-level RST header.
# If not, abort, because the file is probably meant to be included in another file.
if ! grep -q '^=' "$file"; then
    echo "${file} does not contain a top-level RST header."
    echo "No action taken."
    exit 1
fi

# Extract some information from the file.
echo "Extracting information from ${file}."
# Title is calculated as the first line starting with a capital letter that's before a line starting with '='.
title=$(cat $file | tac | grep -A1 '^=' | tac | grep '^[A-Z]' | head -1 )
# Summary is calculated as the first block of regular non-indented text starting with a capital letter, with newlines converted to spaces, some common RST markup stripped out, and consecutive spaces condensed to one.
summary=$(cat $file | tac | sed '/^=/,/^/d' | sed '/^-/,/^/d' | grep -v '^\.\.' | tac | \
    sed -n '/^[A-Z]/,$p' | sed '/^\s*$/,$d' | tr '\n' ' ' | \
    sed 's/`:[^:]*:/`/g' | sed 's/`\([^<]*\) <[^>]*>`/\1/g' | tr -d '_' | tr -d '`' | sed 's/  */ /g' )

# Compute the documentation site URL
html_path="$(echo $file | sed 's/^docs\///' | sed 's/\.rst$//').html"
docs_url="${DOCS_URL}/${html_path}"

# Echo the inputs to the Discouse topic creation request.
echo "Title: ${title}"
echo "Summary: ${summary}"
echo "Embed URL: ${docs_url}"
echo "Discourse URL: ${DISCOURSE_URL}"
echo "Discourse Category: ${DISCOURSE_CATEGORY}"

# Check that all computed values are reasonable
if [ -z "$title" ] || [ -z "$summary" ]; then
    echo "Empty title or summary."
    echo "No action taken."
    exit 1
fi

# Create a new discourse topic.
echo "Creating a discourse topic."
response=$(curl -s -X POST \
  "${DISCOURSE_URL}" \
  -H "Api-Key: ${DISCOURSE_API_KEY}" \
  -H "Api-Username: system" \
  -H "cache-control: no-cache" \
  -F "title=${title}" \
  -F "raw=${summary}" \
  -F "embed_url=${docs_url}" \
  -F "category=${DISCOURSE_CATEGORY}")
echo "Response: ${response}"

# Process the response.
topic_id=$(echo "$response" | jq .topic_id)
echo "Topic ID: ${topic_id}"

# Make sure that the extracted topic ID is a number.
if ! [[ "$topic_id" =~ ^[0-9]+$ ]]; then
    echo "Missing or non-numeric topic ID in response."
    echo "Aborting.";
    exit 1
fi

# Print a confirmation and the topic ID.
echo "Created discourse topic."
echo "Topic ID: ${topic_id}"

# Add the topic ID to the RST file.
echo "Adding reference to new topic to ${file}."
echo "" >> $file
echo ".. discourse::" >> $file
echo "    :topic_identifier: ${topic_id}" >> $file

# Signal success.
echo "Success."
