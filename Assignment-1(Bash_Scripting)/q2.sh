#!/bin/bash

read p

cmds=`compgen -c`

sp=`echo $p | grep -o .| sort | tr -d "\n"`
len=${#sp}

for cmd in $cmds; 
do
	len1=${#cmd}
	if((len==len1));then
		s_cmd=`echo $cmd | grep -o .| sort | tr -d "\n"`
		if [[ "$s_cmd" == "$sp" ]];then
			echo Yes
			echo $cmd
			exit 0
		fi
	fi
done

echo No
