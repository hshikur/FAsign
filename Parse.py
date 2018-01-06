import requests  
from lxml import html

response = requests.get('http://www.bbc.com')

# Parse the body into a tree
parsed_body = html.fromstring(response.text)

# Perform xpaths on the tree
#print parsed_body.xpath('//title/text()') # Get page title  
print parsed_body.xpath('//a/@href') # Get href attribute of all links  ort urllib2

