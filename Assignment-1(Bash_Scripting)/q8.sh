#!/bin/bash

crontab $1 > /tmp/devnull 2>&1

if(($? == 0));then
echo Yes
else
echo No
fi




