#!/bin/bash

DATE=$(date +"%F")

read -p "Please enter a file extension: " EXTENTION

read -p "Please enter a file prefix: (Press Enter for $DATE). " PREFIX

shopt -s nullglob
for file in *.jpg
do
 if [[ ! -z $PREFIX ]];
 then
   mv $file $PREFIX-$file
 else
   mv $file $DATE-$file
 fi
done
shopt -u nullglob
