'''
Created on 4 de jul de 2017

@author: Thiago
'''
from bs4 import BeautifulSoup
import json
import multiprocessing
import re
import sys
import codecs
import time
import os

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

def getPlace(domain, activitytype, cityid, activityid, timeout, maxretries, maxreviews, pause):
    baseurl = 'http://www.tripadvisor.' + domain + '/'+activitytype+'_Review-g'
    orstep = 10
    reviewids = set()
    activitypage = 0
    reviewre = re.compile(r'/ShowUserReviews-g%s-d%s-r([0-9]+)-' % (cityid, activityid))

    while True:
        if maxreviews > 0 and len(reviewids) >= maxreviews:
            break
        if activitypage == 0:
            activitiyurl = '%s%s-d%s' % (baseurl, cityid, activityid)
        else:
            activitiyurl = '%s%s-d%s-or%s' % (baseurl, cityid, activityid, activitypage * orstep)

        htmlpage = download_page(activitiyurl, maxretries, timeout, pause)

        if htmlpage is None:
            print('Error downloading the URL: ' + activitiyurl)
            break
        else:
            return htmlpage.decode('utf-8')

def start_process():
    multiprocessing.current_process()#@UnusedVariable @UndefinedVariable
    
def exec_wrap(data):
    return run(data[0],data[1],data[2],data[3],data[4],data[5],data[6],
               data[7],data[8],data[9],data[10],data[11],data[12])

def run(fields,domain, locationid, activitylocationid, activityid, 
        basepath,argsactivity , argstimeout, argsmaxretries,
        argsmaxreviews,argspause,argsforce,labels):
    
    common_labels = labels['common']
#    common_labels = ['name','@type','priceRange','url']
    adress_labels = labels['adress']
#    adress_labels = ['streetAddress', 'addressLocality', 'addressRegion', 'postalCode']
    aggregateRating_labels = labels['rating']
#    aggregateRating_labels = ['ratingValue','reviewCount']
    row = []
    
    print('crawling: ', ':'.join((domain, locationid, activitylocationid, activityid)))
    if len(fields) == 5:
        reviewids = [fields[4]]
    else:
        place = getPlace(domain, argsactivity, activitylocationid, activityid, 
                                 argstimeout, argsmaxretries, argsmaxreviews, argspause)
        
        soup = BeautifulSoup(place, "html.parser")
        data = soup.find('script', type='application/ld+json').text
                
        jdata = json.loads(data)
        
        ## Common
        for item in common_labels:
            try:
                row.append(jdata[item])
            except KeyError:
                print(":: Key error : " + str(item))
        
        ## Adress
        for item in adress_labels:
            try:
                row.append(jdata['address'][item])
            except KeyError:
                print(":: Key error : " + str(item))
        
        row.append(jdata['address']['addressCountry']['name'])
        
        #Rattings
        for item in aggregateRating_labels:
            try:
                row.append(jdata['aggregateRating'][item])
            except KeyError:
                print(":: Key error : " + str(item))
        
    return row