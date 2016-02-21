#! /bin/bash
# Aditya Mukherjee
# This program will determine the longest common subsequence between the two strings 
# (each string can have a maximum length of 50 characters). 
# NOTE: This subsequence need not be contiguous. 
# The input file may contain empty lines, these need to be ignored.

        #separated1=`echo $string1 | grep -o .`

#        declare -a string2=`echo $line | cut -d  ';' -f2`

input_file=$1
while read -r line; do
    if [[ -n $line ]]; then 
        echo $line
        declare -a sequence_array
        sequence_array[0]=`echo $line | cut -d ';' -f1` 
        sequence_array[1]=`echo $line | cut -d ';' -f2`
        #sequence_array[2]=''  Match between the two sequences
        echo ${sequence_array[@]}
        echo "length of first element :" ${#sequence_array[0]}
        echo "length of second element:" ${#sequence_array[1]}
        for (( a=0; a<=${#sequence_array[0]}; a++)); do
            for (( b=0; b<=${#sequence_array[1]}; b++)); do
                if [ "${sequence_array[0]:$a:1}" = "${sequence_array[1]:$b:1}" ]; then
                    echo "matching sequence: ${sequence_array[0]:$a:1}"
                    #Add More conditions here

                    sequence_array[2]+="${sequence_array[0]:$a:1}"
#
#                    if [ "${#sequence_array[0]:$a}" -gt "1" ];then
#                    #If the matching substring is larger than 1 check to see if it violates sequence order
#         
#
#                            sequence_array[2]+="${sequence_array[0]:$a:1}"
#                            sequence_array[2]+="."
#                            echo ${sequence_array[2]}
#                            echo ${sequence_array[1]} | grep -G ${sequence_array[2]} 
#                            if [ $? -gt 0 ]; then 
#                                echo "sequence not found moving to the next possible solution"
#                            else
#                                echo "match exists"
#                            fi
#                    fi
                fi

            done
        done

    fi
done < "${input_file}"
