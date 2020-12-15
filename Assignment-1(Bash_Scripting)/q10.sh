#!/bin/bash

read operator

read n

case $operator in
+) read num
result=$num
for (( c=2; c<=$n; c++ ))
do
read num
result=`bc <<< "scale = 5;$result+$num"`;
done
;;

-) read num
result=$num
for (( c=2; c<=$n; c++ ))
do
read num
result=`bc <<< "scale = 5;$result-$num"`;
done
;;

/)read num
result=$num
for (( c=2; c<=$n; c++ ))
do
read num
result=`bc <<< "scale = 5;$result/$num"`;
done
;;

*)read num
result=$num
for (( c=2; c<=$n; c++ ))
do
read num 
result=`bc <<< "scale = 5;$result*$num"`;
done
;;

esac
printf "%.4f" $result
