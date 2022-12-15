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

# Adds a discourse topic to all RSTs that need it.

source helpers.sh

for file in $(find . -name '*.rst' | sed 's/^.\///' | grep -Fvxf no-discourse-topic-required.txt); do
    if ! containsDiscourseTopic "$file"; then
        ./add-discourse-topic.sh "$file"
    fi
done
