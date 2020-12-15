#!/bin/bash

read num

num2=`echo $num | sed 's/ //g'`
count=0
sum=0;
len=${#num}
if((len<=1));then
echo Invalid
exit 0
fi

for (( i=${#num2}-1; i>=0; i-- )); do
  ((count+=1))
  val="${num2:$i:1}"
  if ((count%2==0)); then
  	((val=val*2))
  	if((val>=10));then
  		((val-=9))
  	fi
  fi
  ((sum+=val))
done

if((sum%10==0));then
	echo Valid
else
	echo Invalid
fi
