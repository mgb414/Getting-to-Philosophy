# Marcus Bachu
# CodeHS Philosophy Problem


import requests
from bs4 import BeautifulSoup
import sys

MAX_HOPS = 100
GOAL = "https://en.wikipedia.org/wiki/Philosophy"

def is_goal_link(tag):
    return GOAL == tag

def new_link(href):
    return "https://en.wikipedia.org" + str(href)


def valid_link(link):
    print(link)
    if("wikipedia.org/wiki/" not in link):
        print("Sorry invalid starting point")
        return False
    return True

def get_first_link(url):
    with requests.get(url, stream=True) as r:
        soup = BeautifulSoup(r.content, 'html.parser')
        body = soup.find('div', attrs={'id': 'mw-content-text'}).find_all('p')
        for text in body:
            first_link = text.find('a')
            if( first_link is not None):
                return first_link['href']
        return None

def main():
    storage = []
    count = 0
    
    if(len(sys.argv) < 2):
        raise ValueError("Too Few Arguements")
    link = sys.argv[1]

    if(not valid_link(link)):
        return
    
    found  = is_goal_link(link)
    while(not found and count < MAX_HOPS):
        new_href = get_first_link(link)
        link = new_link(new_href)
        found = is_goal_link(link)
        print(link)
        if(link in storage):
            print("Cycle Detected... Aborting")
            break
        storage.append(link)
        count+=1

    if(found):
        print("Congrats")
    else:
        print("Sorry, Philosophy Not Found")

    print("Hops: " + str(count))
        
        

main()
