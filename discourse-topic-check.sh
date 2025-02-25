#
#    Copyright 2022 OICR and UCSC
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        https://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

# This script determines if all changed files rst files in a PR have a discourse topic
source base-branch.sh
source helpers.sh

RETURN_VALUE=0
DOES_NOT_REQUIRE_DISCOURSE_TOPIC=no-discourse-topic-required.txt

if [[ -n $CIRCLE_PULL_REQUEST ]]
then
  # This step requires the variable CIRCLE_PULL_REQUEST to be set to the URL of the PR,
  # this is done automatically in CircleCI.
  # An example value of CIRCLE_PULL_REQUEST is https://github.com/dockstore/dockstore-documentation/pull/209
  pr=$(echo $CIRCLE_PULL_REQUEST | sed 's+https://github.com+https://api.github.com/repos+' | sed 's/pull/pulls/')
  baseBranch="$(curl -s $pr | jq -r '.base.ref')"
fi

for file in $(git diff --name-only "$baseBranch".. | grep "\.rst$" | grep -Fvxf $DOES_NOT_REQUIRE_DISCOURSE_TOPIC)
do
  # The file may be in the base branch but not the current branch. Skip in that case.
  if [[ -f "$file" ]]
  then
    if ! containsDiscourseTopic "$file"
    then
      echo "${file} does not have a discourse topic"
      RETURN_VALUE=1
    fi
  fi
done

if [ $RETURN_VALUE != 0 ]
then
  echo "If your files do not require a discourse topic you can add them to ${DOES_NOT_REQUIRE_DISCOURSE_TOPIC}"
else
  echo "All of the modified files have discourse topics"
fi

exit $RETURN_VALUE
