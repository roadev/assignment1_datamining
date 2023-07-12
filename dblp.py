from bs4 import BeautifulSoup
import requests
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

r = requests.get('https://dblp.org/search?q=data+mining', headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')

results = []

cites = soup.find_all('cite')

for cite in cites:
    title = cite.find('span', class_='title').text
    authors = [author.text for author in cite.find_all('span', itemprop='author')]
    year = cite.find('span', class_='year').text if cite.find('span', class_='year') else ''

    results.append([title, authors, year])

num_results = len(results)

print(f"Number of results: {num_results}")

with open('dblp_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Authors', 'Year'])
    writer.writerows(results)
