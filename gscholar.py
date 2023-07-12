from bs4 import BeautifulSoup
from parsel import Selector
import requests, lxml, os, json

def google_scholar_pagination():
    # to avoid IP banning
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    
    data = []
    while True:
        html = requests.get('https://scholar.google.com/scholar', headers=headers).text
        selector = Selector(text=html)
        print(f'extrecting {params["start"] + 10} page...')
        for result in selector.css('.gs_r.gs_or.gs_scl'):
            title = result.css('.gs_rt').xpath('normalize-space()').get()
            publication_info = result.css('.gs_a').xpath('normalize-space()').get()
            data.append({
                'title': title,
                'publication_info': publication_info,
            })

        if selector.css('.gs_ico_nav_next').get():
            params['start'] += 10
        else:
            break

    print(json.dumps(data, indent = 2, ensure_ascii = False))
            
google_scholar_pagination()

