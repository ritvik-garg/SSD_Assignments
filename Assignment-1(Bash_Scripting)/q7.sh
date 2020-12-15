#!/bin/bash

read n

num=`ps -au | tr -s ' ' | cut -d ' ' -f 2 | wc -l`

ps -au | tr -s ' ' | cut -d ' ' -f 2 | head -$((num)) | tail -$((num-1)) > pid.txt 

cat pid.txt | head -$((n))


