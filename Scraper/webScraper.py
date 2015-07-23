from bs4 import BeautifulSoup
import urllib.request

# Save site url in a variable
URL = "http://smashboards.com/threads/captain-falcon-hitboxes-and-frame-data.284165/"

# Open the url and save the html data into bs4
def request_page(link):
    f = urllib.request.urlopen(link)
    data = f.read()
    webpage = BeautifulSoup(data)
    return webpage

def parse_info(webpage):
    article_tag = webpage.find_all('article',limit = 1)
    print(article_tag.contents)

page = request_page(URL)
parse_info(page)

# Creates a file to hold the data
# dataFile = open(input("Enter the name of the file: ", "w"))
