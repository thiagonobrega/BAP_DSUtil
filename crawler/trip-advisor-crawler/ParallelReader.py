'''
Created on 4 de jul de 2017

@author: Thiago
'''
import multiprocessing
import codecs

def start_process():
    multiprocessing.current_process()#@UnusedVariable @UndefinedVariable
    
def exec_wrap(data):
    return run(data[0],data[1],data[2],data[3],data[4])    
    
def run(filepath,review_labels,rating_label,name_label,adress_labels):
            
    with codecs.open(filepath, mode='r', encoding='utf8') as file:
        htmlpage = file.read()
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(htmlpage, "html.parser")
        data = soup.find('script', type='application/ld+json').text
        import json
            
        jd = json.loads(data)
        review_data = []
        
        try:
            for item in review_labels:
                review_data.append(jd[item])
                    
                #label
                rating_data = jd['reviewRating']
                review_data.append(rating_data[rating_label])
                    
            place = jd['itemReviewed']    
            
            place_data = []
                #label
            place_data.append(place[name_label])
                
            place_addr = place['address']
                #label
            for item in adress_labels:
                place_data.append(place_addr[item])
                    
                #label
            country = place_addr['addressCountry']
            place_data.append(country['name'])
                        
            full_data = place_data + review_data
        except:
            print(":: Error")
            full_data = []
    return full_data