#!/bin/bash

var1=1
count=1
for arg in $@
do
	if [ "$count" == "1" ]; then
		var1=$arg;
		let count+=1
	else
		let var1=$var1**$arg
	fi
done

echo $var1
