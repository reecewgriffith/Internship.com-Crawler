import requests
from bs4 import BeautifulSoup

from InternshipCrawler import InternshipCrawlModule

######################################################################################

InternshipCrawlModule.menu()

choice = input("Please enter the number of your selection:\n")

if choice is '0':
    url = "http://www.internships.com/search/posts?Keywords=marketing%2C%20advertising%2C%20%22social%20media%22%2C%20%22public%20relations%22&page="
elif choice is '1':
    url = "http://www.internships.com/search/posts?Keywords=accounting%2C%20accountant%2C%20bookkeeping%2C%20audit%2C%20%22general%20ledger%22&page="
elif choice is '2':
    url = "http://www.internships.com/search/posts?Keywords=engineering%2C%20architecture&page="
elif choice is '3':
    url = "http://www.internships.com/search/posts?Keywords=finance%2C%20banking%2C%20%22financial%20analyst%22%2C%20investing&page="
elif choice is '4':
    url = "http://www.internships.com/search/posts?Keywords=psychology%2C%20%22mental%20health%22%2C%20counselor&page="
elif choice is '5':
    url = "http://www.internships.com/search/posts?Keywords=law%2C%20legal%2C%20lawyer%2C%20mediation%2C%20paralegal%2C%20attorney&page="
elif choice is '6':
    url = "http://www.internships.com/search/posts?Keywords=biology%2C%20science%2C%20biomedical&page="
elif choice is '7':
    url = "http://www.internships.com/search/posts?Keywords=%22computer%20science%22%2C%20programmer%2C%20%22web%20developer%22%2C%20IT%2C%20developer%2C%20technology%2C%20software&page="
elif choice is '8':
    url = "http://www.internships.com/search/posts?Keywords=art%2C%20design%2C%20photography%2C%20%22graphic%20design%22%2C%20fashion&page="
elif choice is '9':
    url = "http://www.internships.com/search/posts?Keywords=business%2C%20management%2C%20sales%2C%20consulting&page="
else:
    print("Invalid input")
    exit()

InternshipCrawlModule.core_spider(10, url)