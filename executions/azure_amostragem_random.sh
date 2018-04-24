echo ":::: FEII"

mkdir -p /home/thiago/samples/feii/lei
mkdir -p /home/thiago/samples/feii/sec

echo "LEI Simples"
python3 randomSampler.py --infile /home/thiago/dados/fei/parsed_lei.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiago/samples/feii/lei/simples/
echo "LEI Combinado"
python3 randomSampler.py --infile /home/thiago/dados/fei/parsed_lei.csv --nsamples 5 --sample_size 458 916 1833 2749 3665 --outdir /home/thiago/samples/feii/lei/combinado/

echo "SEC Simples"
python3 randomSampler.py --infile /home/thiago/dados/fei/parsed_sec.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiago/samples/feii/sec/simples/
echo "SEC Combinado"
python3 randomSampler.py --infile /home/thiago/dados/fei/parsed_sec.csv --nsamples 5 --sample_size 458 916 1833 2749 3665 --outdir /home/thiago/samples/feii/sec/combinado/

echo ":::: REST"

mkdir -p /home/thiago/samples/Restaurants/trip
mkdir -p /home/thiago/samples/Restaurants/yelp

echo "TRIP Simples"
python3 randomSampler.py --infile /home/thiago/dados/Restaurants/tripadvisor_data.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiago/samples/Restaurants/trip/simples/
echo "TRIP Combinado"
python3 randomSampler.py --infile /home/thiago/dados/Restaurants/tripadvisor_data.csv --nsamples 5 --sample_size 382 765 1530 2295 3060 --outdir /home/thiago/samples/Restaurants/trip/combinado/				

echo "YELP Simples"
python3 randomSampler.py --infile /home/thiago/dados/Restaurants/yelp_data.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiago/samples/Restaurants/yelp/simples/
echo "YELP Combinado"
python3 randomSampler.py --infile /home/thiago/dados/Restaurants/yelp_data.csv --nsamples 5 --sample_size 382 765 1530 2295 3060 --outdir /home/thiago/samples/Restaurants/yelp/combinado/


echo ":::: VOTERS"

mkdir -p /home/thiago/samples/us_voters/nc
mkdir -p /home/thiago/samples/us_voters/oh 


echo "NC Simples"
python3 randomSampler.py --infile /home/thiago/dados/us_voters/ncvoter.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiago/samples/us_voters/nc/simples/
echo "NC Combinado"
python3 randomSampler.py --infile /home/thiago/dados/us_voters/ncvoter.csv --nsamples 5 --sample_size 38988 77976 155952 233928 311903 --outdir /home/thiago/samples/us_voters/nc/combinado/				

echo "OH Simples"
python3 randomSampler.py --infile /home/thiago/dados/us_voters/ohio_voters.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiago/samples/us_voters/oh/simples/
echo "OH Combinado"
python3 randomSampler.py --infile /home/thiago/dados/us_voters/ohio_voters.csv --nsamples 5 --sample_size 38988 77976 155952 233928 311903 --outdir /home/thiago/samples/us_voters/oh/combinado/


echo ":::: PE"

mkdir -p /home/thiago/samples/PublicEmployees/mpog
mkdir -p /home/thiago/samples/PublicEmployees/tce

echo "MPOG Simples"
python3 randomSampler.py --infile /home/thiago/dados/PublicEmployees/mpog.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiago/samples/PublicEmployees/mpog/simples/
echo "MPOG Combinado"
python3 randomSampler.py --infile /home/thiago/dados/PublicEmployees/mpog.csv --nsamples 5 --sample_size 640 1281 2561 3842 4645 --outdir /home/thiago/samples/PublicEmployees/mpog/combinado/				

echo "CGU Simples"
python3 randomSampler.py --infile /home/thiago/dados/PublicEmployees/cgu.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiago/samples/PublicEmployees/cgu/simples/
echo "CGU Combinado"
python3 randomSampler.py --infile /home/thiago/dados/PublicEmployees/cgu.csv --nsamples 5 --sample_size 640 1281 2561 3842 4645 --outdir /home/thiago/samples/PublicEmployees/cgu/combinado/



echo ":::: DRUGS"

mkdir -p /home/thiago/samples/drugs/fda
mkdir -p /home/thiago/samples/drugs/ca

echo "FDA Simples"
python3 randomSampler.py --infile /home/thiago/dados/drugs/drugsfda.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiago/samples/drugs/fda/simples/
echo "FDA Combinado"
python3 randomSampler.py --infile /home/thiago/dados/drugs/drugsfda.csv --nsamples 5 --sample_size 1279 2557 5115 7672 10229 --outdir /home/thiago/samples/drugs/fda/combinado/				

echo "CA Simples"
python3 randomSampler.py --infile /home/thiago/dados/drugs/drugsca.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiago/samples/drugs/ca/simples/
echo "CA Combinado"
python3 randomSampler.py --infile /home/thiago/dados/drugs/drugsca.csv --nsamples 5 --sample_size 1279 2557 5115 7672 10229 --outdir /home/thiago/samples/drugs/ca/combinado/




#echo ":::: SP_Adresses"

#mkdir -p /home/thiago/samples/SP_Adresses/cnefe
#mkdir -p /home/thiago/samples/SP_Adresses/iptu

##/home/thiago/dados/SP_Adresses/parsedcnef.csv 
##observar se o formato da saida do sample
#/home/thiago/dados/SP_Adresses/parsed_iptu.csv

#echo "CNEFE Simples"
#python3 randomSampler.py --infile /home/thiago/dados/SP_Adresses/parsedcnef.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiago/samples/SP_Adresses/cnefe/simples/
#echo "CNEFE Combinado"
#python3 randomSampler.py --infile /home/thiago/dados/SP_Adresses/parsedcnef.csv --nsamples 5 --sample_size 8038 15750 31501 47256 63015  --outdir /home/thiago/samples/SP_Adresses/cnefe/combinado/

#echo "IPTU Simples"
#python3 randomSampler.py --infile /home/thiago/dados/SP_Adresses/parsediptu.csv --nsamples 5 --sample_size 0.0025 0.005 0.01 0.015 0.02 --use-percent --outdir /home/thiago/samples/SP_Adresses/iptu/simples/
#echo "IPTU Combinado"
#python3 randomSampler.py --infile /home/thiago/dados/SP_Adresses/parsediptu.csv --nsamples 5 --sample_size 8038 15750 31501 47256 63015  --outdir /home/thiago/samples/SP_Adresses/iptu/combinado/