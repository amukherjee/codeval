#! /bin/bash
# Aditya Mukherjee

filename=$1

while IFS='' read -r line || [[ -n $line ]]; do
    position=`echo "$line" | awk '{print $NF}'`
    let position=position+1
    echo $line | rev | cut -d ' ' -f $position 
done < "${filename}"
