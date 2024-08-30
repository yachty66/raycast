#!/Users/maxhager/.virtualenvs/base/bin/python

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title url_to_text
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "query" }

# Documentation:
# @raycast.description Takes and url as input and returns all the text from the url.
# @raycast.author Max Hager
# @raycast.authorURL https://twitter.com/MaxHager66

import sys
import pyperclip
import requests
from bs4 import BeautifulSoup

def get_text():
    query = sys.argv[1]
    #query = "https://www.census.gov/data/developers/data-sets/acs-5year.html"
    response = requests.get(query)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        
        # Remove empty lines
        text_lines = [line for line in text.splitlines() if line.strip()]
        cleaned_text = '\n'.join(text_lines)
        
        # Copy the cleaned text to the clipboard
        pyperclip.copy(cleaned_text)
        print("Text copied to clipboard.")
    else:
        print("Failed to retrieve content from the URL")

# Call the function to extract text from the URL provided in the query
get_text()

