# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 15:32:34 2017
This class implements the G-means algorith 
(detailed in D. Pelleg, D. Pelleg, A. W. Moore, and A. W. Moore, “X-means: Extending K-means with efficient estimation of the number of clusters,” Proc. Seventeenth Int. Conf. Mach. Learn. table contents, pp. 727–734, 2000.)

We modify the class provided by Zachary Pustejovsky [1] and modify to cluster textual data...

Zac github link: https://github.com/flylo/g-means

"""
from sampler import ksampler
import scipy as sp
import numpy as np
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.preprocessing import scale


class GMeans(object):
	
    """
        strictness = how strict should the anderson-darling test for normality be
			0: not at all strict
			4: very strict
    """
    def __init__(self, min_obs=10, max_depth=10, random_state=None, strictness=0):
        super(GMeans, self).__init__()
        self.max_depth = max_depth
        self.min_obs = min_obs
        self.random_state = random_state

        if strictness not in range(5):
            raise ValueError("strictness parameter must be integer from 0 to 4")
            
        self.strictness = strictness
        self.stopping_criteria = []
        self.cluster_list = []

	
    def _gaussianCheck(self, vector):
        """
            check whether a given input vector follows a gaussian distribution
            H0: vector is distributed gaussian
            H1: vector is not distributed gaussian
        """
        output = sp.stats.anderson(vector)

        if output[0] <= output[1][self.strictness]:
            return True
        else:
            return False
        
    def _recursiveClustering(self, df, depth, index):
        """
            recursively run kmeans with k=2 on your data until a max_depth is reached or we have
            gaussian clusters
        """
        depth += 1
        if depth == self.max_depth:
            self.data_index[index[:, 0]] = index
            self.stopping_criteria.append('max_depth')
            return
			
        #km = MiniBatchKMeans(n_clusters=2, random_state=self.random_state)
        #km.fit(data)
        X = ksampler.vectorize(df)
        nk=2
        km = ksampler.clusterFiX(df,X,nk)
        
        centers = km.cluster_centers_
        v = centers[0] - centers[1]
        x_prime = scale(X.dot(v) / (v.dot(v)))
        gaussian = self._gaussianCheck(x_prime)
		
		# print gaussian
        if gaussian == True:
            self.data_index[index[:, 0]] = index
            self.stopping_criteria.append('gaussian')
            return

        labels = set(km.labels_)
        for k in labels:
            current_data = df[km.labels_ == k]

            if current_data.shape[0] <= self.min_obs:
                self.data_index[index[:, 0]] = index
                self.stopping_criteria.append('min_obs')
                return
			

            current_index = index[km.labels_==k]
            current_index[:, 1] = np.random.randint(0,1000000000)
            self._recursiveClustering(df=current_data, depth=depth, index=current_index)

		#set_trace()
    
    def fit(self, data):
        """
            fit the recursive clustering model to the data
        """
        self.data = data
        data_index = np.array([(i, False) for i in range(len(data))])
        self.data_index = data_index
        self._recursiveClustering(df=data, depth=0, index=data_index)
        self.labels_ = self.data_index[:, 1]