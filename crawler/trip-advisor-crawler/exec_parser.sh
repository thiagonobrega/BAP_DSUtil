#!/bin/bash
# ./exec_parser.sh US 8

input=$1
process=$2

for f in $input/*; do
    if [[ -d $f ]]; then
	
	#out=`echo $f | awk -F '/' '{print $2}'`
	out=`echo $f | awk -F '/' '{print $NF}'`

	outfile="$out.csv"
	indir="$f/"
	#echo "python3 trip-advisor-parser2.py -d $indir -o $outfile -p $process"
	python3 trip-advisor-parser2.py -d $indir -o $outfile -p $process
    fi
done

