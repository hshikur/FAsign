import sys
import requests
from lxml import html
import urlparse

def get_urls():
	global links,out
	begin_url = 'https://bbc.com'
	response = requests.get(begin_url)
	the_tree = html.fromstring(response.content)
	links = the_tree.xpath('//a')

	out = []
	for link in links:
		if 'href' in link.attrib:
			out.append(link.attrib['href'])
	return out
print(get_urls())

#sys.stdout = open('/home/ubuntu/Desktop/F-secure/urls.txt', 'w')
for url in links:
	l = requests.get(out)
	f = open('/home/ubuntu/Desktop/F-secure/urls.txt', 'w')
	f.write(l.content)
	f.close

