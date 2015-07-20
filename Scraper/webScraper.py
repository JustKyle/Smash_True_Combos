import requests
import json
from bs4 import BeautifulSoup

# Save site url in a variable
URL_Root = "http://wiki.teamliquid.net/"
DEFAULT_DEST = "/smash//Frame_Data"
CHARACTER_LIST = ['Fox','Falco','Sheik','Marth','Jigglypuff','Peach','Captain_Falcon','Luigi','Roy']

# Pull the site into the smashBoards variable
smashBoards = requests.get("")

# Print the status code to verify it worked
print("Status code: " + smashBoards.status_code)

# Store the page content for parsing
pgContent = smashBoards.content

# Get the raw html using BeautifulSoup
soup = BeautifulSoup(pgContent, "html.parser")

# Get information between first two article tags
soup.find_all("article",limit=1)

# Creates a file to hold the data
# dataFile = open(input("Enter the name of the file: ", "w"))
