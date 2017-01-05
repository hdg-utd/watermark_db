import urllib2
from bs4 import BeautifulSoup

url_string = "http://www.watermark.org/message/4400"

try:
	response_code = urllib2.urlopen(url_string).getcode()
	if(response_code != 200):
		print "Not 200"
	else:
		web_page = urllib2.urlopen(url_string).read()
		soup = BeautifulSoup(web_page, "lxml")

		title_parent = soup.findAll('h2', {'class': 'message-title'})[0]
		for title_child in title_parent.children:
			title_string = title_child.contents[0]
		if(title_string != ""):
			date_created = soup.findAll('span', {'class': 'date'})[0].contents[0]
except:
	print "Not connected"