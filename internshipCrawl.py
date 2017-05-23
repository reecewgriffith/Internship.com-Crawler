import requests
from bs4 import BeautifulSoup

######################################################################################

def core_spider(max):
    page = 1

    while page <= max:
        url = "https://www.internships.com/search/posts?Keywords=engineering%2C%20architecture&page=" + str(page)

        source_code = requests.get(url)
        plain_text = source_code.text

        soup = BeautifulSoup(plain_text, "html.parser")

        for link in soup.findAll('a', {'target': '_self'}):
            href = "https://www.internships.com/" + link.get('href')
            title = link.string
            print(title)
            print(href + "\n")
        page += 1

######################################################################################

core_spider(10)