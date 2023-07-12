import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://www.springeropen.com"
search_url = f"{base_url}/search?query=computer+science&searchType=publisherSearch&page="



with open('tableB/tableB.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(['ID', 'title', 'authors', 'abstract', 'url', 'date'])

    id = 1

    for i in range(1, 101):

        res = requests.get(search_url + str(i))
        res.raise_for_status()

        soup = BeautifulSoup(res.text, 'html.parser')
        articles = soup.select("article")

        if len(articles) * i > 1000:
            break

        for article in articles:
            title = article.select_one(".c-listing__title").get_text(strip=True)
            
            urls = article.select(".c-listing__title a")
            url = "; ".join(base_url + u["href"] for u in urls)
            
            authors = article.select_one(".c-listing__authors-list").get_text(strip=True)
            date = article.select_one('[data-test="published-on"] span').get_text(strip=True)
            abstract_paragraph = article.select_one('p')
            abstract = abstract_paragraph.get_text(strip=True) if abstract_paragraph else ""
            writer.writerow([id, title, authors, abstract, url, date])
            id = id + 1
