#!/bin/bash
MY_SHELL="csh"

if [ "$MY_SHELL" = "bash" ]
then
	echo "You seem to like bash shell."
elif [ "$MY_SHELL" = "csh" ]
then
	echo "You seem to like the csh shell."
else
	echo "You dont seem to like bash or csh shell."
fi
