#!/bin/bash

# First command line argument is your readthedocs token. https://readthedocs.org/accounts/tokens/
# Second command line argument is the name of your branch. If you name your branch to include a '/' you will need change it to "-" and uppercase becomes lowercase.
# "feature/testBranch" -> "feature-testbranch"

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

# Activate version
curl -X PATCH "https://readthedocs.org/api/v3/projects/dockstore/versions/$2/" -H "Authorization: Token $1" -H "Content-Type: application/json" -d @activate-body.json

# Build version
curl -d "" -X POST "https://readthedocs.org/api/v3/projects/dockstore/versions/$2/builds/" -H "Authorization: Token $1"