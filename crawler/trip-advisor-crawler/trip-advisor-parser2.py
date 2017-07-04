#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2015 Andrea Esuli (andrea@esuli.it)
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import csv
import os
import re
import sys
import codecs
import fnmatch
import multiprocessing
import ParallelReader



if sys.version_info[0] >= 3:
    import html



def get_review_filesnames(input_dir):
    for root, dirnames, filenames in os.walk(input_dir):
        for filename in fnmatch.filter(filenames, '*.html'):
            yield os.path.join(root, filename)    


if __name__ == '__main__':
    # sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
    parser = argparse.ArgumentParser(
        description='TripAdvisor Restaurant parser')
    parser.add_argument('-d', '--dir', help='Directory with the data for parsing', required=True)
    parser.add_argument('-o', '--outfile', help='Output file path for saving the reviews in csv format', required=True)
    parser.add_argument('-p', '--process',  action='store', dest='process', type=int,  help='Number of process', default=4)

    args = parser.parse_args()
    pool_size = int(args.process)
    print("POOL SIZE : " + str(pool_size) )
    
    #labels
    review_labels = ['author','datePublished','reviewBody']
    rating_label = 'ratingValue'
    name_label = 'name'
    adress_labels = ['streetAddress', 'addressLocality', 'addressRegion', 'postalCode']
    country_label = 'country'
    
    #multiprocessor
    pool = multiprocessing.Pool(processes=pool_size, initializer=ParallelReader.start_process )#@UnusedVariable @UndefinedVariable
    job_args = []    
    file_list = get_review_filesnames(args.dir)
    
    i = 0
#     totalf = len(file_list)
    import time
    t0 = time.time()
    for filepath in file_list:
        job_args.append([filepath,review_labels,rating_label,name_label,adress_labels])
        i += 1
        if i % 1000 == 0:
            delta = time.time()-t0
            print(str(i) + " in " + str(delta) + " s")
            t0 = time.time()
    
    t0 = time.time()
    print("Start computation")
    pool_outputs = pool.map(ParallelReader.exec_wrap, job_args )
    pool.close()  # no more tasks
    pool.join()  # wrap up current tasks
    delta = time.time()-t0
    print("End computation in " + str(delta) + " s")

    #print(pool_outputs)    
    t0 = time.time()
    print("Writing csv")    
    with codecs.open(args.outfile, 'w', encoding='utf8') as out:
        writer = csv.writer(out, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC  ,lineterminator='\n')
        for row in pool_outputs:
            writer.writerow(row)
    
    delta = time.time()-t0
    print("Done writing csv in " + str(delta) + " s!")
