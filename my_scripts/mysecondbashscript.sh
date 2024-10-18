#!/bin/bash

date
echo Hello, $USER
pwd
ps -ef | grep 'bioset' | wc -l
ls -la /etc/passwd | awk '{print $1}'


