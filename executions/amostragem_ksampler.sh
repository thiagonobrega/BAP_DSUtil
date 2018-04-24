echo ":::: SP_Adresses"
echo "CNEFE Simples"
python3 kSampler2.py --infile /home/thiagonobrega/zexp/odata/SP_Adresses/parsed_cnef.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiagonobrega/zexp/samples/SP_Adresses/cnefe/ksimples/
echo "CNEFE Combinado"
python3 kSampler2.py --infile /home/thiagonobrega/zexp/odata/SP_Adresses/parsed_cnef.csv --nsamples 5 --sample_size 8038 15750 31501 47256 63015  --outdir /home/thiagonobrega/zexp/samples/SP_Adresses/cnefe/kcombinado/

echo "IPTU Simples"
python3 kSampler2.py --infile /home/thiagonobrega/zexp/odata/SP_Adresses/parsed_iptu.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiagonobrega/zexp/samples/SP_Adresses/iptu/ksimples/
echo "IPTU Combinado"
python3 kSampler2.py --infile /home/thiagonobrega/zexp/odata/SP_Adresses/parsed_iptu.csv --nsamples 5 --sample_size 8038 15750 31501 47256 63015  --outdir /home/thiagonobrega/zexp/samples/SP_Adresses/iptu/kcombinado/


echo ":::: FEII"

mkdir -p /home/thiagonobrega/zexp/samples/feii/lei
mkdir -p /home/thiagonobrega/zexp/samples/feii/sec

echo "LEI Simples"
python3 kSampler2.py --infile /home/thiagonobrega/zexp/odata/feii/parsed_lei.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiagonobrega/zexp/samples/feii/lei/ksimples/
echo "LEI Combinado"
python3 kSampler2.py --infile /home/thiagonobrega/zexp/odata/feii/parsed_lei.csv --nsamples 5 --sample_size 458 916 1833 2749 3665 --outdir /home/thiagonobrega/zexp/samples/feii/lei/kcombinado/

echo "SEC Simples"
python3 kSampler2.py --infile /home/thiagonobrega/zexp/odata/feii/parsed_sec.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiagonobrega/zexp/samples/feii/sec/ksimples/
echo "SEC Combinado"
python3 kSampler2.py --infile /home/thiagonobrega/zexp/odata/feii/parsed_sec.csv --nsamples 5 --sample_size 458 916 1833 2749 3665 --outdir /home/thiagonobrega/zexp/samples/feii/sec/kcombinado/


echo ":::: DRUGS"

mkdir -p /home/thiagonobrega/zexp/samples/drugs/fda
mkdir -p /home/thiagonobrega/zexp/samples/drugs/ca

echo "FDA Simples"
python3 kSampler2.py --infile /home/thiagonobrega/zexp/odata/drugs/drugs_fda.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiagonobrega/zexp/samples/drugs/fda/ksimples/
echo "FDA Combinado"
python3 kSampler2.py --infile /home/thiagonobrega/zexp/odata/drugs/drugs_fda.csv --nsamples 5 --sample_size 17221 34443 68886 103328 137771 --outdir /home/thiagonobrega/zexp/samples/drugs/fda/kcombinado/				

echo "CA Simples"
python3 kSampler2.py --infile /home/thiagonobrega/zexp/odata/drugs/drugs_ca.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiagonobrega/zexp/samples/drugs/ca/ksimples/
echo "CA Combinado"
python3 kSampler2.py --infile /home/thiagonobrega/zexp/odata/drugs/drugs_ca.csv --nsamples 5 --sample_size 17221 34443 68886 103328 137771 --outdir /home/thiagonobrega/zexp/samples/drugs/ca/kcombinado/


echo ":::: PE"

mkdir -p /home/thiagonobrega/zexp/samples/PublicEmployees/mpog
mkdir -p /home/thiagonobrega/zexp/samples/PublicEmployees/tce

echo "MPOG Simples"
python3 kSampler2.py --infile /home/thiagonobrega/zexp/odata/PublicEmployees/mpog.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiagonobrega/zexp/samples/PublicEmployees/mpog/ksimples/
echo "MPOG Combinado"
python3 kSampler2.py --infile /home/thiagonobrega/zexp/odata/PublicEmployees/mpog.csv --nsamples 5 --sample_size 2082 4164 8328 12492 16657 --outdir /home/thiagonobrega/zexp/samples/PublicEmployees/mpog/kcombinado/				

echo "TCE Simples"
python3 kSampler2.py --infile /home/thiagonobrega/zexp/odata/PublicEmployees/tce.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiagonobrega/zexp/samples/PublicEmployees/tce/ksimples/
echo "TCE Combinado"
python3 kSampler2.py --infile /home/thiagonobrega/zexp/odata/PublicEmployees/tce.csv --nsamples 5 --sample_size 2082 4164 8328 12492 16657 --outdir /home/thiagonobrega/zexp/samples/PublicEmployees/tce/kcombinado/


echo ":::: REST"

mkdir -p /home/thiagonobrega/zexp/samples/Restaurants/trip
mkdir -p /home/thiagonobrega/zexp/samples/Restaurants/yelp

echo "TRIP Simples"
python3 kSampler2.py --infile /home/thiagonobrega/zexp/odata/Restaurants/tripadvisor_data.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiagonobrega/zexp/samples/Restaurants/trip/ksimples/
echo "TRIP Combinado"
python3 kSampler2.py --infile /home/thiagonobrega/zexp/odata/Restaurants/tripadvisor_data.csv --nsamples 5 --sample_size 382 765 1530 2295 3060 --outdir /home/thiagonobrega/zexp/samples/Restaurants/trip/kcombinado/				

echo "YELP Simples"
python3 kSampler2.py --infile /home/thiagonobrega/zexp/odata/Restaurants/yelp_data.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiagonobrega/zexp/samples/Restaurants/yelp/ksimples/
echo "YELP Combinado"
python3 kSampler2.py --infile /home/thiagonobrega/zexp/odata/Restaurants/yelp_data.csv --nsamples 5 --sample_size 382 765 1530 2295 3060 --outdir /home/thiagonobrega/zexp/samples/Restaurants/yelp/kcombinado/


echo ":::: VOTERS"

mkdir -p /home/thiagonobrega/zexp/samples/us_voters/nc
mkdir -p /home/thiagonobrega/zexp/samples/us_voters/oh 


echo "NC Simples"
python3 kSampler2.py --infile /home/thiagonobrega/zexp/odata/us_voters/ncvoter.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiagonobrega/zexp/samples/us_voters/nc/ksimples/
echo "NC Combinado"
python3 kSampler2.py --infile /home/thiagonobrega/zexp/odata/us_voters/ncvoter.csv --nsamples 5 --sample_size 38988 77976 155952 233928 311903 --outdir /home/thiagonobrega/zexp/samples/us_voters/nc/kcombinado/				

echo "OH Simples"
python3 kSampler2.py --infile /home/thiagonobrega/zexp/odata/us_voters/ohio_voters.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiagonobrega/zexp/samples/us_voters/oh/ksimples/
echo "OH Combinado"
python3 kSampler2.py --infile /home/thiagonobrega/zexp/odata/us_voters/ohio_voters.csv --nsamples 5 --sample_size 38988 77976 155952 233928 311903 --outdir /home/thiagonobrega/zexp/samples/us_voters/oh/kcombinado/