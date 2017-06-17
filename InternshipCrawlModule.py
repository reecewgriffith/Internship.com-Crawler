import requests
from bs4 import BeautifulSoup

######################################################################################

#web crawl function
def core_spider(max, url):
    page = 1
    
    #gets a max of 10 pages as defined in main
    while page <= max:
        url = url + str(page)

        source_code = requests.get(url)
        plain_text = source_code.text

        soup = BeautifulSoup(plain_text, "html.parser")

        for link in soup.findAll('a', {'target': '_self'}):
            href = "https://www.internships.com/" + link.get('href')
            title = link.string
            print(title)
            print(href + "\n")
        page += 1

#simple menu function
def menu():
    print("Welcome to the Internship.com web-crawler.\n")

    print("This program will give you a master list of all the links for availiable internships based on the catergory you select.")
    print("This will save you lots of time looking through oage after page.")
    print("The program will give you a master list with internships links and titles without all the clutter!\n")

    print("0. Marketing\n1. Accounting\n2. Engineering\n3. Finance\n4. Psychology")
    print("5. Law\n6. Biology\n7.Computer Science\n8. Art & Design\n9. Business\n")
