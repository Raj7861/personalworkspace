#!/bin/bash
old=$(cd)
[ $# -eq 0 ] && exit 1
[ -d $1 ] && cd $1 || echo exit 2

# nullglob : If set, bash allows patterns which match no files to expand to a null string, rather than themselves.
shopt -s nullglob
found=0
for i in *.jpg;
do
  echo "File $i found"
  found=1
done
shopt -u nullglob

[ $found -eq 0 ] && echo "Directory is empty"
cd $old
