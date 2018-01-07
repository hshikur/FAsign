import requests
from lxml import html
import urlparse
import sys

def get_urls():
	begin_url = 'https://bbc.com'
	response = requests.get(begin_url)
	the_tree = html.fromstring(response.content)
	links = the_tree.xpath('//a')

	out = []
	for link  in links:
		if 'href' in link.attrib:
			out.append(link.attrib['href'])
	return out
print(get_urls())

#links = [urlparse.urljoin(response.url, url) for url in links]  
#print 'Found %s urls' % len(links)


for url in links[:]:
	l = requests.get(url)
	f = open('/home/ubuntu/Desktop/F-secure/urls.txt/%s' % url.split('/')[-1], 'w')
	f.write(l.content)
	f.close
