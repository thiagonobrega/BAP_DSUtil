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
import os
import re
import sys
import codecs
import time
import multiprocessing
import ParallelCrawler

if sys.version_info[0] >= 3:
    import urllib
    import urllib.request as request
    import urllib.error as urlerror
else:
    import urllib2 as request
    import urllib2 as urlerror
import socket
from contextlib import closing
from time import sleep


def download_page(url, maxretries, timeout, pause):
    tries = 0
    htmlpage = None
    while tries < maxretries and htmlpage is None:
        try:
            with closing(request.urlopen(url, timeout=timeout)) as f:
                htmlpage = f.read()
                sleep(pause)
        except (urlerror.URLError, socket.timeout, socket.error):
            tries += 1
    return htmlpage


def getactivityids(domain, activitytype, locationid, timeout, maxretries, pause):
    baseurl = 'http://www.tripadvisor.' + domain + '/'+activitytype+'s-g'
    oastep = 30
    activityids = set()
    citypage = 0
    activityre = re.compile(r'/'+activitytype+'_Review-g([0-9]+)-d([0-9]+)-Reviews')

    while True:
        if citypage == 0:
            cityurl = '%s%s' % (baseurl, locationid)
        else:
            cityurl = '%s%s-oa%s' % (baseurl, locationid, citypage * oastep)

        htmlpage = download_page(cityurl, maxretries, timeout, pause)

        if htmlpage is None:
            print('Error downloading the city URL: ' + cityurl)
            break
        else:
            pageids = set(activityre.findall(htmlpage.decode('utf-8')))
            allin = True
            for id_ in pageids:
                if not id_ in activityids:
                    allin = False
                    break
            if allin:
                break
            activityids.update(pageids)
            citypage += 1

    return activityids

activities = ['Hotel','Restaurant']

def main():
    # sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
    parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description='''ID format:
    domain:locationcode
    e.g. com:187768 reviews of hotels in Italy from the com domain
    domain:locationcode:citycode
    e.g. jp:187899:187899 city of Pisa from the jp domain
    domain:locationcode:citycode:hotelcode
    e.g. it:187899:187899:662603 all reviews for a specific hotel from the it domain
    domain:locationcode:citycode:hotelcode:reviewcode
    e.g. it:187899:187899:662603:322965103 a specific review''')
    parser.add_argument('-f', '--force', help='Force download even if already successfully downloaded', required=False,
                        action='store_true')
    parser.add_argument('-a', '--activity', help='Type of activity to crawl (default: %s)' % activities[0], choices=activities,
                        default=activities[0])
    parser.add_argument(
            '-r', '--maxretries', help='Max retries to download a file. Default: 3',
            required=False, type=int, default=3)
    parser.add_argument(
            '-t', '--timeout', help='Timeout in seconds for http connections. Default: 180',
            required=False, type=int, default=180)
    parser.add_argument(
            '-p', '--pause', help='Seconds to wait between http requests. Default: 0.2', required=False, default=0.2,
            type=float)
    parser.add_argument(
            '-m', '--maxreviews', help='Maximum number of reviews per item to download. Default:unlimited',
            required=False,
            type=int, default=-1)
    parser.add_argument(
            '-o', '--out', help='Output base path', required=True)
    parser.add_argument('ids', metavar='ID', nargs='+',
                        help='IDs for which to download reviews')
    
    parser.add_argument(
            '-c', '--concurrent', help='Concurrent downloads. Default :8',
            required=False, type=int, default=3)
    args = parser.parse_args()

    basepath = args.out
    pool_size = args.concurrent
    
    if not os.path.exists(basepath):
        os.makedirs(basepath)

    with open(os.path.join(args.out, 'ids.txt'), 'w') as file:
        for id in args.ids:
            print('input: ', id)
            fields = id.split(':')
            domain = fields[0]
            locationid = fields[1]
            
            t0 = time.time()
            if len(fields) == 2:
                activityids = getactivityids(domain, args.activity, locationid, args.timeout, args.maxretries, args.pause)
            elif len(fields) >= 4:
                activityids = [(fields[2], fields[3])]
            
            t1 = time.time()
            delta = t1 - t0
            print(":: list of itens to download fetched in " + str(delta) + "s with " + str(len(activityids)) + " elements")
            #multiprocessing
            pool = multiprocessing.Pool(processes=pool_size, initializer=ParallelCrawler.start_process )#@UnusedVariable @UndefinedVariable
            job_args = []
            print(":: Crawling " + locationid )
            for activitylocationid, activityid in sorted(activityids):
                
                iargs = [fields,domain, locationid, activitylocationid, activityid, 
                        basepath,args.activity , args.timeout, args.maxretries,
                        args.maxreviews,args.pause,args.force]
                job_args.append([fields,domain, locationid, activitylocationid, activityid, 
                        basepath ,args.activity , args.timeout, args.maxretries,
                        args.maxreviews,args.pause,args.force])
                
            print(":: Downloading " + locationid )
            pool_outputs = pool.map(ParallelCrawler.exec_wrap, job_args )
            for line in pool_outputs:
                file.write(line)
                file.write("\n")
                
            pool.close()  # no more tasks
            pool.join()  # wrap up current tasks
            
            t0 = time.time()
            delta = t0 - t1
            print(":: Download done in " + str(delta) + "s")

if __name__ == '__main__':
    #com:g46919 small
    #com:g31377 big
    main()
