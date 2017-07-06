'''
Created on 4 de jul de 2017

@author: Thiago
'''
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

def getreviewids(domain, activitytype, cityid, activityid, timeout, maxretries, maxreviews, pause):
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
            pageids = set(reviewre.findall(htmlpage.decode('utf-8')))
            allin = True
            for id in pageids:
                if not id in reviewids:
                    allin = False
                    break

            if allin:
                break
            if maxreviews > 0 and len(reviewids) + len(pageids) > maxreviews:
                n = len(reviewids) + len(pageids) - maxreviews
                pageids = list(pageids)
                del pageids[-n:]
                pageids = set(pageids)

            reviewids.update(pageids)
            activitypage += 1

    return reviewids


def getreview(domain, cityid, activity, reviewid, timeout, maxretries, basepath, force, pause):
    baseurl = 'http://www.tripadvisor.' + domain + '/ShowUserReviews-g'
    reviewurl = '%s%s-d%s-r%s' % (baseurl, cityid, activity, reviewid)

    path = os.sep.join((basepath, domain, str(cityid), str(activity)))
    filename = os.sep.join((path, str(reviewid) + '.html'))
    if force or not os.path.exists(filename):
        htmlpage = download_page(reviewurl, maxretries, timeout, pause)

        if htmlpage is None:
            print('Error downloading the review URL: ' + reviewurl)
        else:
            if not os.path.exists(path):
                os.makedirs(path)

            with codecs.open(filename, mode='w', encoding='utf8') as file:
                file.write(htmlpage.decode('utf-8'))

def start_process():
    multiprocessing.current_process()#@UnusedVariable @UndefinedVariable
    
def exec_wrap(data):
    return run(data[0],data[1],data[2],data[3],data[4],data[5],data[6],
               data[7],data[8],data[9],data[10],data[11])    

def run(fields,domain, locationid, activitylocationid, activityid, 
        basepath,argsactivity , argstimeout, argsmaxretries,
        argsmaxreviews,argspause,argsforce):
    
    file_output = [] 
    
    print('crawling: ', ':'.join((domain, locationid, activitylocationid, activityid)))
    if len(fields) == 5:
        reviewids = [fields[4]]
    else:
        reviewids = getreviewids(domain, argsactivity, activitylocationid, activityid, 
                                 argstimeout, argsmaxretries, argsmaxreviews, argspause)
        for reviewid in sorted(reviewids):
            print('downloading: ', ':'.join((domain, locationid, activitylocationid, activityid, reviewid)))
            log = ':'.join((domain, locationid, activitylocationid, activityid, reviewid))
#             log = str(log) + "\n"
            file_output.append(log)
            getreview(domain, activitylocationid, activityid, reviewid,
                      argstimeout, argsmaxretries, basepath, argsforce,argspause)

    return file_output