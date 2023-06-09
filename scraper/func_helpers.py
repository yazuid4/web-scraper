import requests
from bs4 import BeautifulSoup
import re

def scraper(urlx, keywords):
    resp = requests.get(urlx)
    pars = BeautifulSoup(resp.content, 'html.parser')

    for tag in pars.find_all(['script', 'style']):
        tag.decompose()   
        
    bod = pars.find_all('body')    
    results = bod[0].find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p'])
    
    ans = []
    
    if len(keywords) > 0:
        for res in results:
            str_temp = res.text
            str_temp = str_temp.strip()
            str_temp = " ".join(str_temp.split())
            if len(str_temp) > 0:
                for key in keywords:
                    if key.lower() in str_temp.lower():
                        ans.append(str_temp + '\n\n')
    else:
        for res in results:
            str_temp = res.text
            str_temp = str_temp.strip()
            str_temp = " ".join(str_temp.split())
            if len(str_temp) > 0:
                ans.append(str_temp + '\n\n')

    return ans



def isValidUrl(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(regex, url) != None

