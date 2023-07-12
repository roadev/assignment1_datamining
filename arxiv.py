import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://arxiv.org"

def clean_text(text):
    return ' '.join(text.split())

data = []

for start in range(0, 1000, 50):
    search_url = f"{base_url}/search/?query=data+mining&searchtype=all&start={start}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    results = soup.find_all('li', {'class': 'arxiv-result'})

    for result in results:
        title = clean_text(result.find('p', {'class': 'title is-5 mathjax'}).text.strip())

        authors_elem = result.find('p', {'class': 'authors'})
        first_span = authors_elem.find('span')

        if first_span is not None:
            first_span.decompose()

        authors = clean_text(authors_elem.text.strip())

        abstract = clean_text(result.find('span', {'class': 'abstract-full has-text-grey-dark mathjax'}).text.strip())

        pub_url = "https://arxiv.org" + result.find('p', {'class': 'list-title is-inline-block'}).find('a')['href']

        submitted_date_dirty = result.find('p', {'class': 'is-size-7'}).text.split(';')[-1].strip()
        submitted_date = submitted_date_dirty.replace('originally announced', '').rstrip('.').strip()
        
        data.append([title, authors, abstract, pub_url, submitted_date])

with open('tableA/tableA.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['title', 'authors', 'abstract', 'url', 'date'])
    writer.writerows(data)
