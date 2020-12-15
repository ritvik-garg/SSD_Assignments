#!/bin/bash

read var;

echo $var | tr -s "()" " " | sed 's/ $//' | sed 's/^ //' | sed 's/^/(/' | sed 's/$/)/'
