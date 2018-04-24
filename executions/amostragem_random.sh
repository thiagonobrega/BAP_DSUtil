echo ":::: SP_Adresses"

mkdir -p /home/thiagonobrega/zexp/samples/SP_Adresses/cnefe
mkdir -p /home/thiagonobrega/zexp/samples/SP_Adresses/iptu

#/home/thiagonobrega/zexp/odata/SP_Adresses/parsed_cnef.csv 
#observar se o formato da saida do sample
#/home/thiagonobrega/zexp/odata/SP_Adresses/parsed_iptu.csv

echo "CNEFE Simples"
python3 randomSampler.py --infile /home/thiagonobrega/zexp/odata/SP_Adresses/parsed_cnef.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiagonobrega/zexp/samples/SP_Adresses/cnefe/simples/
echo "CNEFE Combinado"
python3 randomSampler.py --infile /home/thiagonobrega/zexp/odata/SP_Adresses/parsed_cnef.csv --nsamples 5 --sample_size 8038 15750 31501 47256 63015  --outdir /home/thiagonobrega/zexp/samples/SP_Adresses/cnefe/combinado/

echo "IPTU Simples"
python3 randomSampler.py --infile /home/thiagonobrega/zexp/odata/SP_Adresses/parsed_iptu.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiagonobrega/zexp/samples/SP_Adresses/iptu/simples/
echo "IPTU Combinado"
python3 randomSampler.py --infile /home/thiagonobrega/zexp/odata/SP_Adresses/parsed_iptu.csv --nsamples 5 --sample_size 8038 15750 31501 47256 63015  --outdir /home/thiagonobrega/zexp/samples/SP_Adresses/iptu/combinado/


echo ":::: FEII"

mkdir -p /home/thiagonobrega/zexp/samples/feii/lei
mkdir -p /home/thiagonobrega/zexp/samples/feii/sec

echo "LEI Simples"
python3 randomSampler.py --infile /home/thiagonobrega/zexp/odata/feii/parsed_lei.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiagonobrega/zexp/samples/feii/lei/simples/
echo "LEI Combinado"
python3 randomSampler.py --infile /home/thiagonobrega/zexp/odata/feii/parsed_lei.csv --nsamples 5 --sample_size 458 916 1833 2749 3665 --outdir /home/thiagonobrega/zexp/samples/feii/lei/combinado/

echo "SEC Simples"
python3 randomSampler.py --infile /home/thiagonobrega/zexp/odata/feii/parsed_sec.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiagonobrega/zexp/samples/feii/sec/simples/
echo "SEC Combinado"
python3 randomSampler.py --infile /home/thiagonobrega/zexp/odata/feii/parsed_sec.csv --nsamples 5 --sample_size 458 916 1833 2749 3665 --outdir /home/thiagonobrega/zexp/samples/feii/sec/combinado/


echo ":::: DRUGS"

mkdir -p /home/thiagonobrega/zexp/samples/drugs/fda
mkdir -p /home/thiagonobrega/zexp/samples/drugs/ca

echo "FDA Simples"
python3 randomSampler.py --infile /home/thiagonobrega/zexp/odata/drugs/drugs_fda.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiagonobrega/zexp/samples/drugs/fda/simples/
echo "FDA Combinado"
python3 randomSampler.py --infile /home/thiagonobrega/zexp/odata/drugs/drugs_fda.csv --nsamples 5 --sample_size 17221 34443 68886 103328 137771 --outdir /home/thiagonobrega/zexp/samples/drugs/fda/combinado/				

echo "CA Simples"
python3 randomSampler.py --infile /home/thiagonobrega/zexp/odata/drugs/drugs_ca.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiagonobrega/zexp/samples/drugs/ca/simples/
echo "CA Combinado"
python3 randomSampler.py --infile /home/thiagonobrega/zexp/odata/drugs/drugs_ca.csv --nsamples 5 --sample_size 17221 34443 68886 103328 137771 --outdir /home/thiagonobrega/zexp/samples/drugs/ca/combinado/


echo ":::: PE"

mkdir -p /home/thiagonobrega/zexp/samples/PublicEmployees/mpog
mkdir -p /home/thiagonobrega/zexp/samples/PublicEmployees/tce

echo "MPOG Simples"
python3 randomSampler.py --infile /home/thiagonobrega/zexp/odata/PublicEmployees/mpog.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiagonobrega/zexp/samples/PublicEmployees/mpog/simples/
echo "MPOG Combinado"
python3 randomSampler.py --infile /home/thiagonobrega/zexp/odata/PublicEmployees/mpog.csv --nsamples 5 --sample_size 2082 4164 8328 12492 16657 --outdir /home/thiagonobrega/zexp/samples/PublicEmployees/mpog/combinado/				

echo "TCE Simples"
python3 randomSampler.py --infile /home/thiagonobrega/zexp/odata/PublicEmployees/tce.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiagonobrega/zexp/samples/PublicEmployees/tce/simples/
echo "TCE Combinado"
python3 randomSampler.py --infile /home/thiagonobrega/zexp/odata/PublicEmployees/tce.csv --nsamples 5 --sample_size 2082 4164 8328 12492 16657 --outdir /home/thiagonobrega/zexp/samples/PublicEmployees/tce/combinado/


echo ":::: REST"

mkdir -p /home/thiagonobrega/zexp/samples/Restaurants/trip
mkdir -p /home/thiagonobrega/zexp/samples/Restaurants/yelp

echo "TRIP Simples"
python3 randomSampler.py --infile /home/thiagonobrega/zexp/odata/Restaurants/tripadvisor_data.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiagonobrega/zexp/samples/Restaurants/trip/simples/
echo "TRIP Combinado"
python3 randomSampler.py --infile /home/thiagonobrega/zexp/odata/Restaurants/tripadvisor_data.csv --nsamples 5 --sample_size 382 765 1530 2295 3060 --outdir /home/thiagonobrega/zexp/samples/Restaurants/trip/combinado/				

echo "YELP Simples"
python3 randomSampler.py --infile /home/thiagonobrega/zexp/odata/Restaurants/yelp_data.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiagonobrega/zexp/samples/Restaurants/yelp/simples/
echo "YELP Combinado"
python3 randomSampler.py --infile /home/thiagonobrega/zexp/odata/Restaurants/yelp_data.csv --nsamples 5 --sample_size 382 765 1530 2295 3060 --outdir /home/thiagonobrega/zexp/samples/Restaurants/yelp/combinado/


echo ":::: VOTERS"

mkdir -p /home/thiagonobrega/zexp/samples/us_voters/nc
mkdir -p /home/thiagonobrega/zexp/samples/us_voters/oh 


echo "NC Simples"
python3 randomSampler.py --infile /home/thiagonobrega/zexp/odata/us_voters/ncvoter.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiagonobrega/zexp/samples/us_voters/nc/simples/
echo "NC Combinado"
python3 randomSampler.py --infile /home/thiagonobrega/zexp/odata/us_voters/ncvoter.csv --nsamples 5 --sample_size 38988 77976 155952 233928 311903 --outdir /home/thiagonobrega/zexp/samples/us_voters/nc/combinado/				

echo "OH Simples"
python3 randomSampler.py --infile /home/thiagonobrega/zexp/odata/us_voters/ohio_voters.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiagonobrega/zexp/samples/us_voters/oh/simples/
echo "OH Combinado"
python3 randomSampler.py --infile /home/thiagonobrega/zexp/odata/us_voters/ohio_voters.csv --nsamples 5 --sample_size 38988 77976 155952 233928 311903 --outdir /home/thiagonobrega/zexp/samples/us_voters/oh/combinado/