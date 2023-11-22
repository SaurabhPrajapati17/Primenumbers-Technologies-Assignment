import requests
from bs4 import BeautifulSoup

url = "https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787"
req = requests.get(url)

soup = BeautifulSoup(req.content, "html.parser")
print(soup.prettify())


# this code is written to get the all HTML element so, that it become easy to scrape the website.