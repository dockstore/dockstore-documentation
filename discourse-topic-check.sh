
echo "develop second"
git diff --name-only --diff-filter=A ${CIRCLE_BRANCH}..develop
echo "develop first"
git diff --name-only --diff-filter=A develop..${CIRCLE_BRANCH}