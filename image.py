import requests  
from lxml import html  
import sys  
import urlparse


#get request from bbc.com and store it to response variable
response = requests.get('http://bbc.com/', timeout=20)  
#html module to parse it and save the results in a XML tree
parsed_body = html.fromstring(response.content)

# Grab links to all images, locates information using path experssions to select node or node-sets
images = parsed_body.xpath('//img/@src')  

# If there is no image
if not images:  
    sys.exit("Found No Images")

# Convert any relative urls to absolute urls
images = [urlparse.urljoin(response.url, url) for url in images]  
print 'Found %s images' % len(images)

# download all
for url in images[:]:  
    r = requests.get(url)
    f = open('/home/henok/Desktop/F-secure/Images/%s' % url.split('/')[-1], 'w')
    f.write(r.content)
    f.close()

