#!/bin/sh
# variables to use in sh file
my_name='王芳豪'
echo "Hello" $my_name

# args for loading in
for args in $*;do
    echo "my argument : " $args
done

echo "success!"

