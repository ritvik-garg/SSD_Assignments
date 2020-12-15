#!/bin/bash

cat ~/.bash_history | tail -10 | awk '{print $1}' | sort | uniq -c | sort -rn | head -10 | awk '{print $2 " " $1}'
