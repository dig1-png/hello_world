#!/bin/sh
# learn list in bash

list=(1 2 3 4 5)
for item in ${list[@]}
do
    echo "list content :" $item
done
