#time bash -x exp1.sh |& tee log_exp1.txt
#####
##### Random
#####
#abt
python3 randomSampler.py --infile /home/thiago/exp/data/full_data/gregos/abt/abt.csv --nsamples 5 --sample_size 50 100 250 500 --outdir samples/abt/
python3 randomSampler.py --infile /home/thiago/exp/data/full_data/gregos/abt/abt.csv --nsamples 5 --sample_size 0.05 0.1 0.25 0.5 --use-percent --outdir samples/abt/
#buy
python3 randomSampler.py --infile /home/thiago/exp/data/full_data/gregos/buy/buy.csv --nsamples 5 --sample_size 50 100 250 500 --outdir samples/buy/
python3 randomSampler.py --infile /home/thiago/exp/data/full_data/gregos/buy/buy.csv --nsamples 5 --sample_size 0.05 0.1 0.25 0.5 --use-percent --outdir samples/buy/ 
#acm
python3 randomSampler.py --infile /home/thiago/exp/data/full_data/gregos/acm/bacm.csv --nsamples 5 --sample_size 50 100 250 500 --outdir samples/acm/
python3 randomSampler.py --infile /home/thiago/exp/data/full_data/gregos/acm/bacm.csv --nsamples 5 --sample_size 0.05 0.1 0.25 0.5 --use-percent --outdir samples/acm/ 
#amazon (rever tamanhos)
python3 randomSampler.py --infile /home/thiago/exp/data/full_data/gregos/amazon/amazon.csv --nsamples 5 --sample_size 50 100 250 500 --outdir samples/amazon/
python3 randomSampler.py --infile /home/thiago/exp/data/full_data/gregos/amazon/amazon.csv --nsamples 5 --sample_size 0.05 0.1 0.25 0.5 --use-percent --outdir samples/amazon/ 
#dblp
python3 randomSampler.py --infile /home/thiago/exp/data/full_data/gregos/dblp/adblp.csv --nsamples 5 --sample_size 50 100 500 1000 --outdir samples/dblp/
python3 randomSampler.py --infile /home/thiago/exp/data/full_data/gregos/dblp/adblp.csv --nsamples 5 --sample_size 0.05 0.1 0.25 0.5 --use-percent --outdir samples/dblp/ 
python3 randomSampler.py --infile /home/thiago/exp/data/full_data/gregos/dblp/bdblp.csv --nsamples 5 --sample_size 50 100 250 500 --outdir samples/dblp/
python3 randomSampler.py --infile /home/thiago/exp/data/full_data/gregos/dblp/bdblp.csv --nsamples 5 --sample_size 0.05 0.1 0.25 0.5 --use-percent --outdir samples/dblp/ 
#google
python3 randomSampler.py --infile /home/thiago/exp/data/full_data/gregos/google/google.csv --nsamples 5 --sample_size 50 100 250 500 --outdir samples/google/
python3 randomSampler.py --infile /home/thiago/exp/data/full_data/gregos/google/google.csv --nsamples 5 --sample_size 0.05 0.1 0.25 0.5 --use-percent --outdir samples/goole/ 
#scholar
python3 randomSampler.py --infile /home/thiago/exp/data/full_data/gregos/scholar/scholar.csv --nsamples 5 --sample_size 50 100 500 1000 --outdir samples/scholar/
python3 randomSampler.py --infile /home/thiago/exp/data/full_data/gregos/scholar/scholar.csv --nsamples 5 --sample_size 0.05 0.1 0.25 0.5 --use-percent --outdir samples/scholar/ 
#####
##### Bernoulli
#####
#abt
python3 bernoulliSampler.py --infile /home/thiago/exp/data/full_data/gregos/abt/abt.csv --nsamples 5 --p_size 0.05 0.1 0.25 0.5 --outdir samples/abt/
#buy
python3 bernoulliSampler.py --infile /home/thiago/exp/data/full_data/gregos/buy/buy.csv --nsamples 5 --p_size 0.05 0.1 0.25 0.5 --outdir samples/buy/
#acm
python3 bernoulliSampler.py --infile /home/thiago/exp/data/full_data/gregos/acm/bacm.csv --nsamples 5 --p_size 0.05 0.1 0.25 0.5 --outdir samples/acm/
#amazon
python3 bernoulliSampler.py --infile /home/thiago/exp/data/full_data/gregos/amazon/amazon.csv --nsamples 5 --p_size 0.05 0.1 0.25 0.5 --outdir samples/amazon/
#dblp
python3 bernoulliSampler.py --infile /home/thiago/exp/data/full_data/gregos/dblp/adblp.csv --nsamples 5 --p_size 0.05 0.1 0.25 0.5 --outdir samples/dblp/
python3 bernoulliSampler.py --infile /home/thiago/exp/data/full_data/gregos/dblp/bdblp.csv --nsamples 5 --p_size 0.05 0.1 0.25 0.5 --outdir samples/dblp/
#google
python3 bernoulliSampler.py --infile /home/thiago/exp/data/full_data/gregos/google/google.csv --nsamples 5 --p_size 0.05 0.1 0.25 0.5 --outdir samples/google/
#scholar
python3 bernoulliSampler.py --infile /home/thiago/exp/data/full_data/gregos/scholar/scholar.csv --nsamples 5 --p_size 0.05 0.1 0.25 0.5 --outdir samples/scholar/
#####
##### K-sampler
#####
#abt
python3 kSampler2.py --infile /home/thiago/exp/data/full_data/gregos/abt/abt.csv --nsamples 5 --sample_size 50 100 250 500 --outdir samples/abt/
python3 kSampler2.py --infile /home/thiago/exp/data/full_data/gregos/abt/abt.csv --nsamples 5 --sample_size 0.05 0.1 0.25 0.5 --use-percent --outdir samples/abt/ 
#buy
python3 kSampler2.py --infile /home/thiago/exp/data/full_data/gregos/buy/buy.csv --nsamples 5 --sample_size 50 100 250 500 --outdir samples/buy/
python3 kSampler2.py --infile /home/thiago/exp/data/full_data/gregos/buy/buy.csv --nsamples 5 --sample_size 0.05 0.1 0.25 0.5 --use-percent --outdir samples/buy/ 
#acm
python3 kSampler2.py --infile /home/thiago/exp/data/full_data/gregos/acm/bacm.csv --nsamples 5 --sample_size 50 100 250 500 --outdir samples/acm/
python3 kSampler2.py --infile /home/thiago/exp/data/full_data/gregos/acm/bacm.csv --nsamples 5 --sample_size 0.05 0.1 0.25 0.5 --use-percent --outdir samples/acm/ 
#amazon (rever tamanhos)
python3 kSampler2.py --infile /home/thiago/exp/data/full_data/gregos/amazon/amazon.csv --nsamples 5 --sample_size 50 100 250 500 --outdir samples/amazon/
python3 kSampler2.py --infile /home/thiago/exp/data/full_data/gregos/amazon/amazon.csv --nsamples 5 --sample_size 0.05 0.1 0.25 0.5 --use-percent --outdir samples/amazon/ 
#dblp
python3 kSampler2.py --infile /home/thiago/exp/data/full_data/gregos/dblp/adblp.csv --nsamples 5 --sample_size 50 100 500 1000 --outdir samples/dblp/
python3 kSampler2.py --infile /home/thiago/exp/data/full_data/gregos/dblp/adblp.csv --nsamples 5 --sample_size 0.05 0.1 0.25 0.5 --use-percent --outdir samples/dblp/ 
python3 kSampler2.py --infile /home/thiago/exp/data/full_data/gregos/dblp/bdblp.csv --nsamples 5 --sample_size 50 100 250 500 --outdir samples/dblp/
python3 kSampler2.py --infile /home/thiago/exp/data/full_data/gregos/dblp/bdblp.csv --nsamples 5 --sample_size 0.05 0.1 0.25 0.5 --use-percent --outdir samples/dblp/ 
#google
python3 kSampler2.py --infile /home/thiago/exp/data/full_data/gregos/google/google.csv --nsamples 5 --sample_size 50 100 250 500 --outdir samples/google/
python3 kSampler2.py --infile /home/thiago/exp/data/full_data/gregos/google/google.csv --nsamples 5 --sample_size 0.05 0.1 0.25 0.5 --use-percent --outdir samples/google/ 
#scholar
python3 kSampler2.py --infile /home/thiago/exp/data/full_data/gregos/scholar/scholar.csv --nsamples 5 --sample_size 50 100 500 1000 --outdir samples/scholar/
python3 kSampler2.py --infile /home/thiago/exp/data/full_data/gregos/scholar/scholar.csv --nsamples 5 --sample_size 0.05 0.1 0.25 0.5 --use-percent --outdir samples/scholar/ 

