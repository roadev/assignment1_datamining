import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://www.springeropen.com"
search_url = f"{base_url}/search?query=computer+science&searchType=publisherSearch&page="

with open('tableB/tableB.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['title', 'authors', 'abstract', 'url', 'date'])

    for i in range(1, 101):

        res = requests.get(search_url + str(i))
        res.raise_for_status()

        soup = BeautifulSoup(res.text, 'html.parser')
        articles = soup.select("article")

        # Exit the loop after scraping 1000 articles
        if len(articles) * i > 1000:
            break

        for article in articles:
            title = article.select_one(".c-listing__title").get_text(strip=True)
            url = base_url + article.select_one(".c-listing__title a")["href"]
            authors = article.select_one(".c-listing__authors-list").get_text(strip=True)
            date = article.select_one('[data-test="published-on"] span').get_text(strip=True)
            abstract_paragraph = article.select_one('p')
            abstract = abstract_paragraph.get_text(strip=True) if abstract_paragraph else "Abstract not found"
            writer.writerow([title, authors, abstract, url, date])
