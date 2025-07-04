from bs4 import BeautifulSoup
import requests


# Specify url
luc_url = 'https://www.luc.edu/accreditation/index.shtml'

# Package the request, send the request and catch the response
r = requests.get(luc_url)

# Extract the response as html: html_doc
luc_html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
#soup = BeautifulSoup(luc_html_doc)
soup = BeautifulSoup(luc_html_doc , "lxml")

# Get the title of the webpage
luc_title = soup.title

# Print the title of the webpage
print("Here is the title of the webpage: " , luc_title)

# Get webpage's text
luc_text = soup.get_text()

# Find all 'a' tags (which define hyperlinks)
a_tags = soup.find_all('a')

# Print the URLs to the shell
for link in a_tags:
    print("Here is a list of all the URLs: " ,(link.get('href')))

# Print text to the shell
print("Here is all the text of the webpage: " ,(luc_text))
