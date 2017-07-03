import requests
import re
from bs4 import BeautifulSoup
states_1 = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

states_2 = {
    "Alabama" : "AL",
    "Alaska":"AK",
    "Arizona":"AZ",
    "Arkansas":"AR",
    "California":"CA",
    "Colorado":"CO",
    "Connecticut":"CT",
    "Delaware":"DE",
    "District of Columbia":"DC",
#    "Columbia":"DC",
    "Florida":"FL",
    "Georgia":"GA",
    "Hawaii":"HI",
    "Idaho":"ID",
    "Illinois":"IL",
    "Indiana":"IN",
    "Iowa":"IA",
    "Kansas":"KS",
    "Kentucky":"KY",
    "Louisiana":"LA",
    "Maine":"ME",
    "Montana":"MT",
    "Nebraska":"NE",
    "Nevada":"NV",
    "New Hampshire":"NH",
#    "Hampshire":"NH",
    "New Jersey":"NJ",
#    "Jersey":"NJ",
    "New Mexico":"NM",
#    "Mexico":"NM",
    "New York":"NY",
#    "York":"NY",
    "North Carolina":"NC",
#    "NorthCarolina":"NC",
    "North Dakota":"ND",
#    "NorthDakota":"ND",
    "Ohio":"OH",
    "Oklahoma":"OK",
    "Oregon":"OR",
    "Maryland":"MD",
    "Massachusetts":"MA",
    "Michigan":"MI",
    "Minnesota":"MN",
    "Mississippi":"MS",
    "Missouri":"MO",
    "Pennsylvania":"PA",
    "Rhode Island":"RI",
    "South Carolina":"SC",
#    "SouthCarolina":"SC",
    "South Dakota":"SD",
#    "SouthDakota":"SD",
    "Tennessee":"TN",
    "Texas":"TX",
    "Utah":"UT",
    "Vermont":"VT",
    "Virginia":"VA",
    "Washington":"WA",
    "West Virginia":"WV",
    "Wisconsin":"WI",
    "Wyoming":"WY",
}

def getState(state):
    try:
        state = states_2[state]
    except KeyError:
        state = 'ZZ'
    return state

trick_state2 = ["Dakota","Carolina","York","Mexico","Hampshire"]
trisck_state3 = ["Columbia"]

trick_states = trick_state2 + trisck_state3
    

base_url = 'https://www.tripadvisor.com/'  ## we need this to join the links later ##
main_page = 'https://www.tripadvisor.com/Attractions-g255057-Activities-oa{}-Canberra_Australian_Capital_Territory-Hotels.html#ATTRACTION_LIST_CONTENTS'
main_page = "https://www.tripadvisor.com.br/Restaurants-g191-oa{}-United_States.html#LOCATION_LIST"
links = []

## get the initial page to find the number of pages ##
r = requests.get(main_page.format(0))  
soup = BeautifulSoup(r.text, "html.parser")
## select the last page from the list of pages ('a', {'class':'pageNum taLnk'}) ##
last_page = max([ int(page.get('data-offset')) for page in soup.find_all('a', {'class':'pageNum taLnk'}) ])

## now iterate over that range (first page, last page, number of links), and extract the links from each page ##
for i in range(0, last_page + 20, 20):
    page = main_page.format(i)
    soup = BeautifulSoup(requests.get(page).text, "html.parser") ## get the next page and parse it with BeautifulSoup ##  
    ## get the hrefs from ('div', {'class':'listing_title'}), and join them with base_url to make the links ##geo_name
    #links += [ base_url + link.find('a').get('href') for link in soup.find_all('div', {'class':'listing_title'}) ]
    #links += [ link.find('a').get('href') for link in soup.find_all('div', {'class':'geo_name'}) ]


    #links += [ link.find('a').get('href') for link in soup.find(attrs={'class':'geoList'}).find_all('a')]
    for ulist in soup.find_all('ul', {'class':'geoList'}):
        for link in ulist.find_all('a'):
            #print(link.get('href'))
            links.append(link.get('href'))
    
    #links += [ link.find('a').get('href') for link in soup.find_all('ul', {'class':'geoList'}) ]
    print("@"+str(i)+"#"+str(last_page)+"="+str(len(links)))


for link in links:
    data = re.split('-',link)
    id = data[1]
    location = re.split('\.',data[2])[0]
    
    ldata = re.split('_',location)
    
    #finding state
    i = len(ldata)-1
    state = ldata[i]
    if state in trick_states:
        if state in trisck_state3:
            state = ldata[i-2] + " " + ldata[i-1] + " " + state
            i -= 2
#            print(states_2[state])
            state = getState(state)

        if state in trick_state2:
            state = ldata[i-1] + " " + state
            i -= 1
#            print(states_2[state])
            state = getState(state)
    else:
        state = getState(state)
        #state = states_2[state]
    
    #finding city
    if state == 'ZZ':
        city = "ZZ"
    else:
        city = ""
        for j in range(0,i):
            city += ldata[j]

    print("com:"+id+"#"+state+"#"+city)