# Determines if a file has a discourse topic

function containsDiscourseTopic {
  local fileToCheck="$1"
  grep -A1 "^.. discourse::" $fileToCheck | tail -n1 | grep -E "^( )*:topic_identifier:( )*[0-9]+" > /dev/null
  if [ $? != 0 ]
  then
    return 1
  else
    return 0
  fi
}

