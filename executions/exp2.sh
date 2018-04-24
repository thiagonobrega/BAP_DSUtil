#trip
python3 randomSampler.py --infile /home/thiago/exp/data/full_data/restaurants/trip.csv --nsamples 5 --sample_size 100 1000 5000 10000 --outdir samples/trip/
python3 randomSampler.py --infile /home/thiago/exp/data/full_data/restaurants/trip.csv --nsamples 5 --sample_size 0.01 0.05 0.1 0.2 --outdir samples/trip/ --use-percent
python3 bernoulliSampler.py --infile /home/thiago/exp/data/full_data/restaurants/trip.csv --nsamples 5 --p_size 0.01 0.05 0.1 0.2 --outdir samples/trip/
python3 kSampler2.py --infile /home/thiago/exp/data/full_data/restaurants/trip.csv --nsamples 5 --sample_size 100 1000 5000 10000 --outdir samples/trip/
python3 kSampler2.py --infile /home/thiago/exp/data/full_data/restaurants/trip.csv --nsamples 5 --sample_size 0.01 0.05 0.1 0.2 --outdir samples/trip/ --use-percent
#yelp
python3 randomSampler.py --infile /home/thiago/exp/data/full_data/restaurants/yelp.csv --nsamples 5 --sample_size 100 1000 5000 10000 --outdir samples/yelp/
python3 randomSampler.py --infile /home/thiago/exp/data/full_data/restaurants/yelp.csv --nsamples 5 --sample_size 0.01 0.05 0.1 0.2 --outdir samples/yelp/ --use-percent
python3 bernoulliSampler.py --infile /home/thiago/exp/data/full_data/restaurants/yelp.csv --nsamples 5 --p_size 0.01 0.05 0.1 0.2 --outdir samples/yelp/
python3 kSampler2.py --infile /home/thiago/exp/data/full_data/restaurants/yelp.csv --nsamples 5 --sample_size 100 1000 5000 10000 --outdir samples/yelp/
python3 kSampler2.py --infile /home/thiago/exp/data/full_data/restaurants/yelp.csv --nsamples 5 --sample_size 0.01 0.05 0.1 0.2 --outdir samples/yelp/ --use-percent

#ncvoter
python3 randomSampler.py --infile /home/thiago/exp/data/full_data/voters/ncvoter.csv --nsamples 5 --sample_size 1000 10000 10000 100000 --outdir samples/ncvoter/
python3 randomSampler.py --infile /home/thiago/exp/data/full_data/voters/ncvoter.csv --nsamples 5 --sample_size 0.005 0.01 0.05 0.1 --outdir samples/ncvoter/ --use-percent
python3 bernoulliSampler.py --infile /home/thiago/exp/data/full_data/voters/ncvoter.csv --nsamples 5 --p_size 0.005 0.01 0.05 0.1 --outdir samples/ncvoter/
python3 kSampler2.py --infile /home/thiago/exp/data/full_data/voters/ncvoter.csv --nsamples 5 --sample_size 1000 10000 10000 100000 --outdir samples/ncvoter/
python3 kSampler2.py --infile /home/thiago/exp/data/full_data/voters/ncvoter.csv --nsamples 5 --sample_size 0.005 0.01 0.05 0.1 --outdir samples/ncvoter/ --use-percent
#ohiovoters
python3 randomSampler.py --infile /home/thiago/exp/data/full_data/voters/ohiovoters.csv --nsamples 5 --sample_size 1000 10000 10000 100000 --outdir samples/ohiovoters/
python3 randomSampler.py --infile /home/thiago/exp/data/full_data/voters/ohiovoters.csv --nsamples 5 --sample_size 0.005 0.01 0.05 0.1 --outdir samples/ohiovoters/ --use-percent
python3 bernoulliSampler.py --infile /home/thiago/exp/data/full_data/voters/ohiovoters.csv --nsamples 5 --p_size 0.005 0.01 0.05 0.1 --outdir samples/ohiovoters/
python3 kSampler2.py --infile /home/thiago/exp/data/full_data/voters/ohiovoters.csv --nsamples 5 --sample_size 1000 10000 10000 100000 --outdir samples/ohiovoters/
python3 kSampler2.py --infile /home/thiago/exp/data/full_data/voters/ohiovoters.csv --nsamples 5 --sample_size 0.005 0.01 0.05 0.1 --outdir samples/ohiovoters/ --use-percent





