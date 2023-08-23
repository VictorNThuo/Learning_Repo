from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Find all the <span> tags with class="comments"
span_tags = soup.find_all('span', class_='comments')

# Initialize the sum
total_sum = 0

for span_tag in span_tags:
    # Extract the text content of the span tag
    number_text = span_tag.contents[0]
    
    # Convert the text content to an integer and add it to the sum
    number = int(number_text)
    total_sum += number

print('Sum of numbers:', total_sum)
