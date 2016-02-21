#! /bin/bash 


number=$1
reverse=`echo $number |rev`

if [ "$number" -eq "$reverse" ] 
then
    echo  $number
fi
