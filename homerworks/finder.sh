#!/bin/bash

set -e

read -p "Enter file name: " file
a=$(echo $(find $file))
echo $a
if test -z $a;
then
	echo "No files in system"
fi
md5sum $a
