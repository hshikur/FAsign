import requests
from lxml import html
import urlparse

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


for url in links[:]:
	l = requests.get(url)
#	f = open('/home/ubuntu/Desktop/F-secure/Urls/urls.txt' % url.split('/')[-1], 'w')
	f = open('/home/ubuntu/Desktop/F-secure/Urls/urls.txt', 'w')
	f.write(l.content)
	f.close

