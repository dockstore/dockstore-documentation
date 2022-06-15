
# Determines if a file has a discourse topic
function containsDiscourseTopic {
  grep -A1 "^.. discourse::" $fileToCheck | tail -n1 | grep -E "^( )*:topic_identifier:( )+[0-9]+" > /dev/null
  if [ $? != 0 ]
  then
    echo "${fileToCheck} does not have a discourse topic"
    return 1
  else
    return 0
  fi
}

RETURN_VALUE=0
BASE_BRANCH=develop
CURRENT_BRANCH=
DOES_NOT_REQUIRE_DISCOURSE_TOPIC=no-discourse-required.txt

for file in $(git diff --name-only develop.. | grep -E "*\.rst" | grep -Fvxf $DOES_NOT_REQUIRE_DISCOURSE_TOPIC)
do
  fileToCheck=$file
  if ! containsDiscourseTopic
  then
    RETURN_VALUE=1
  fi
done

if [ $RETURN_VALUE != 0 ]
then
  echo "If your files do not require a discourse topic you can add them to ${DOES_NOT_REQUIRE_DISCOURSE_TOPIC}"
fi

exit $RETURN_VALUE