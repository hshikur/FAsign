import urllib2
from bs4 import BeautifulSoup
import urlparse

page = BeautifulSoup(urllib2.urlopen("http://www.BBC.com"))
for link in page.find_all('a'):
#    print(link.get('href'))
#     print(page.get_text())
    f = open('/home/ubuntu/Desktop/F-secure/urls.txt/%s' % url.split('/')[-1], 'w')
    f.write(r.content)
    f.close()
