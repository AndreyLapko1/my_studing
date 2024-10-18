#!/bin/bash

set -e

read -p "Enter ping address: " address
limit=100

while True
do
	ping_res=$(ping $address | awk '{print $5}' | awk -F "=" '{print $2}' | sed 's/ms//')
	#echo $ping_res
	a=$(ping $address | awk '{print $5}' | awk -F "=" '{print $2}' | cut -c -2 | cut -d' ' -f2)
	for i in {1..4}
	do
		c=$(echo $a | cut -d' ' -f$i)
		echo $c
		if ['$c' -ge '$limit'];
		then
			echo "Ping more then 36"
		else
			echo "Ping succesfully"
		fi
	done
done
