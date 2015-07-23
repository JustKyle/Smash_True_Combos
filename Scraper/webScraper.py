from bs4 import BeautifulSoup
import requests

# Save site url in a variable
URL = "http://smashboards.com/threads/captain-falcon-hitboxes-and-frame-data.284165/"

# Open the url and save the html data into bs4
def request_page(link):
    r = requests.get(link)
    data = r.text
    webpage = BeautifulSoup(data, 'html.parser')
    return webpage

def parse_info(webpage):
    print(webpage.article.text)

page = request_page(URL)
parse_info(page)

# Creates a file to hold the data
# dataFile = open(input("Enter the name of the file: ", "w"))
