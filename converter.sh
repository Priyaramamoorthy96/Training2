#!/bin/bash
read -p "Enter the file name : " file1
B=${file1:0:${#file1}-3}
C="$B""txt"
catdoc $file1>$C
