# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:56:09 2017

@author: Thiago
"""

#Script from http://veekaybee.github.io/how-big-of-a-sample-size-do-you-need/ on how to calculate sample size, adjusted for my own population size
#and confidence intervals
#Original here: http://bc-forensics.com/?p=15

import math
 
# SUPPORTED CONFIDENCE LEVELS: 50%, 68%, 90%, 95%, and 99%
confidence_level_constant = [50,.67], [68,.99], [90,1.64], [95,1.96], [99,2.57]
 
# CALCULATE THE SAMPLE SIZE
def sample_size(population_size, confidence_level, confidence_interval):
  Z = 0.0
  p = 0.5
  e = confidence_interval/100.0
  N = population_size
  n_0 = 0.0
  n = 0.0
 
  # LOOP THROUGH SUPPORTED CONFIDENCE LEVELS AND FIND THE NUM STD
  # DEVIATIONS FOR THAT CONFIDENCE LEVEL
  for i in confidence_level_constant:
    if i[0] == confidence_level:
      Z = i[1]
 
  if Z == 0.0:
    return -1
 
  # CALC SAMPLE SIZE
  n_0 = ((Z**2) * p * (1-p)) / (e**2)
 
  # ADJUST SAMPLE SIZE FOR FINITE POPULATION
  n = n_0 / (1 + ((n_0 - 1) / float(N)) )
 
  return int(math.ceil(n)) # THE SAMPLE SIZE
 
def main():
  sample_sz = 0
  population_sz = 37623+115369
  population_sz = 2*7000000
  confidence_level = 95.0
  #Margin of error/confidence interval - How far away are you willing to be from the population statistic?
  confidence_interval = 2.0
 
  sample_sz = sample_size(population_sz, confidence_level, confidence_interval)
 
  print("SAMPLE SIZE: %d" % sample_sz)
 

def Z(confidence,universe):
    from scipy import stats
    return stats.t._ppf((1+confidence)/2., universe)


### Paper Israel
def cochran_sampleSize(p,e,confidence_level,universe):
    """
        Z2 : is the abscissa of the normal curve that cuts off an area α at the tails (1 - α equals the desired confidence level, e.g., 95%)        
        e : is the desired level of precision (5%)
        p : (maximum variability) is the estimated proportion of an attribute that is present in the population, 
        q : is 1-p
    """
    q = 1 - p
    Z2 = Z(confidence_level,universe) ** 2
    return (Z2 * p * q) / (e ** 2)


def finitePopulationCorrectionForProportions(p,e,confidence_level,universe):
    """
        If the population is small then the sample size can be reduced slightly. This is because a given sample size provides proportionately more information for a small population than for a large population
    """
    n0 = cochran_sampleSize(p,e,confidence_level,universe)
    return (n0)/ (1 + ( (n0-1)/universe ))
        

def yamane(e,universe):
    """
        e : is the desired level of precision (5%)
        p : (maximum variability) is the estimated proportion of an attribute that is present in the population, 
    """
    return universe / (1 + (universe * (e ** 2)) )

### Paper x


if __name__ == "__main__":
#  main()
   
   confidence_level = 95.0
   confidence_interval = 2.0
   p1 = 1000000
   p2 = 700000
   population_size = p1 + p2
   
   ss = sample_size(population_size, confidence_level, confidence_interval)
   print("CONJUNTA : [%i,%i,%i,%i,%i]" % ( int(ss/4), int(ss/2) , int(ss) ,int(ss * 4) , int(ss*8)))
   ss = sample_size(p1, confidence_level, confidence_interval)
   print("p1 : [%i,%i,%i,%i,%i]" % ( int(ss/4), int(ss/2) , int(ss) ,int(ss * 4) , int(ss*8)))
   ss = sample_size(p2, confidence_level, confidence_interval)
   print("p2 : [%i,%i,%i,%i,%i]" % ( int(ss/4), int(ss/2) , int(ss) ,int(ss * 4) , int(ss*8)))
  
#  import numpy as np
#  stats.zscore(np.array([.95]))
#  sp.stats.t._ppf((1+confidence)/2., n-1)
  
#  cochran_sampleSize(.5,.05,.95,370000)
#  finitePopulationCorrectionForProportions(.5,.05,.95,32000)
  
#  yamane(0.05,320000)
  
  
