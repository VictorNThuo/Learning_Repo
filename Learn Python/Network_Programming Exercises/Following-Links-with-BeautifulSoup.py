import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Function to get the last name after following links for a number of repetitions
def get_last_name(url, position, repetitions):
    for _ in range(repetitions):
        # Fetch the HTML content of the current URL
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')

        # Retrieve all of the anchor tags
        tags = soup('a')
        if len(tags) >= position:
            url = tags[position - 1].get('href', None)  # Get the URL from the specified position
        else:
            print("Position out of range")
            return None

    last_name = url.split('/')[-1]  # Extract last part of the URL as the last name
    return last_name

# Input from user
url = input('Enter starting URL: ')
position = int(input('Enter position: '))
repetitions = int(input('Enter number of repetitions: '))

# Get the last name using the defined function
last_name = get_last_name(url, position, repetitions)
if last_name:
    print(f"The last name found after {repetitions} repetitions is: {last_name}")
