#!/bin/bash

dir=$1

if [ -f "$dir" ]
then
	echo "0"
elif [ -d "$dir" ]
then 
	echo "1"
else
	echo "2"
fi
