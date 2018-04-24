in=$1
out=$2

sed 's/;//g' $in >> tt
sed 's/://g' tt > t
rm tt
sed 's/\",\"/\";\"/g' t > tt

awk -F';' -v OFS=';' '
  NR == 1 {print "KeyCol", $0; next}
  {print (NR-1), $0}
' tt > $out

rm t
rm tt
