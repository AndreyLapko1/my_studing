#!/bin/bash

set -e

read -p "Enter ping address: " address
limit=40
counter_fails=0


while True
do
	a=$(ping $address | awk '{print $5}' | awk -F "=" '{print $2}' | cut -c -2 | cut -d' ' -f2)
	for i in {1..4}
	do
		c=$(echo $a | cut -d' ' -f$i)
		if test -z $c;
		then
			echo "Fail!!!"
		else
			if (($c > $limit));
			then
			echo "Ping more then $limit, $c"
			else
			echo "Ping succesfully: $c"
			fi


		fi

		echo $a

		if test -z $c;
		then
		let  "counter_fails = counter_fails + 1"
		fi

		if (($counter_fails > 3));
		then
		echo "Warning!!!! More then 3 fails!!!!!"
		counter_fails=0
		fi
		sleep 1
	done

done
