#!/bin/bash


set -e
s="/opt/290724-ptm/AndreyLapko/hw"

for i in {1..10}
	do
	date +"%H:%M:%S"
	ps -ef |wc -l
#	sleep 5
	done

sudo cat /proc/cpuinfo | grep "model name" >> $s/procinfo.txt
sudo cat /etc/os-release | grep "NAME" | head -1 >> $s/procinfo.txt
sudo cat /etc/os-release | grep "NAME" | head -1 | sed 's/NAME=//' >> $s/procinfo.txt

for j in {50..100}
	do
	touch $s/$j.txt
	done
