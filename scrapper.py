from termios import OPOST
import requests
from bs4 import BeautifulSoup

url = "https://www.ceneo.pl/63490289#tab=reviews"
response = requests.get(url)

page = BeautifulSoup(response.text, 'html.parser')

opinions = page.select("div.js_product-review")
opinion = opinions.pop(0)
opinion_id = opinion["data-entry-id"]
author = opinion.select_one('span.user-post__author-name').get_text().strip()

recomendations = opinion.select_one('span.user-post__author-recomendation > em').get_text()

star_amount = opinion.select_one('span.user-post__score-count').get_text()

opinion_text = opinion.select_one('div.user-post__text').get_text()

print(opinion_text)


