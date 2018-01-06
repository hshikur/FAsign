import urllib2
from bs4 import BeautifulSoup

page = BeautifulSoup(urllib2.urlopen("http://www.BBC.com"))
for link in page.find_all('a'):
#    print(link.get('href'))
     print(page.get_text())
