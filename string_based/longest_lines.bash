#! /bin/bash

filename=$1
limit=`cat ${filename}| awk 'NR == 1'`
cat ${filename} | awk '{print length, ":", $0}'| sort -nr| head -${limit} |  cut -d ":" -f 2 | sed -e 's/^[ \t]*//'
