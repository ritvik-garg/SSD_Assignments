#!/bin/bash

read var
var2=`echo "${var,,}"`;
var3=`echo $var2 | rev`;
if [ "$var3" = "$var2" ]; then
	echo Yes
else
	echo No
fi
