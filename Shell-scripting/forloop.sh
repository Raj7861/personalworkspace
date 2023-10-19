#!/bin/bash

COLORS="red green blue"
DATE=$(date +%F)

for COLOR in $COLORS
do
	echo "COLOR: ${DATE}-$COLOR"
done
