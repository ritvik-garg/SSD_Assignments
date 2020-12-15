#!/bin/bash

mkdir Assignment1 && cd "$_"

touch lab{1..5}.txt

ls *.txt | xargs -i -exec sh -c 'filename="{}"; mv -- "$filename" "${filename%.txt}.c"' \;

ls -lhSr

find ~ -maxdepth 2

find . -name "*.txt"
