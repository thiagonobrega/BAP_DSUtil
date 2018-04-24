#!/bin/bash
IFS="#"

input=$1
outputdir=$2

while read id state city
do
        op="$outputdir/$state/$city/"
        mkdir -p $op
        t=`date`
        echo "@ Saving files in $op"
        echo "@ Executing $id at $t"
        python3 trip-advisor-crawler.py -a Restaurant -p 0.05 -o $op $id
        t=`date`
        echo "@ Exec $id end at $t"
        #python3 trip-advisor-parser.py -a Restaurant -p 0.05 -d .cdata/com/ -o z.txt

done < $input