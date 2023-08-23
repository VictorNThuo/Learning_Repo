from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Ask the user for the URL of the page to scrape
url = input('Enter URL: ')

# Fetch the HTML content from the provided URL
html = urlopen(url, context=ctx).read()

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html, "html.parser")

# Find all the <span> tags with class="comments"
span_tags = soup.find_all('span', class_='comments')

# Initialize the sum to keep track of the total
total_sum = 0

# Iterate through each <span> tag found
for span_tag in span_tags:
    # Extract the text content of the <span> tag
    number_text = span_tag.contents[0]
    
    # Convert the extracted text content to an integer
    number = int(number_text)
    
    # Add the extracted number to the total sum
    total_sum += number

# Print the final sum of the extracted numbers
print('Sum of numbers:', total_sum)