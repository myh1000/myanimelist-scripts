#!/bin/sh

malpost () {
  b=$(python malpost.py conan)
  if [ "$b" == "Updated" ];
  then
    echo $b
  else
    sleep 4
    malpost
  fi
}
malpost
