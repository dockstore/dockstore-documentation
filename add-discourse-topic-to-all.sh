#!/bin/bash

source helpers.sh

for file in $(find . -name '*.rst' | sed 's/^.\///' | grep -Fvxf no-discourse-topic-required.txt); do
    if ! containsDiscourseTopic "$file"; then
        ./add-topic-to-rst.sh "$file"
    fi
done
