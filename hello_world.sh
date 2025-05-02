#!/bin/bash

set -x

# store data in a variable
mesg="Hello World!"

# print variable to the screen w/ echo
echo $mesg

# print variable (2nd method)
# echo ${mesg}

echo "Who do you want to say hello to?"

read person

echo Hello ${person}

echo $1
