import urllib2
from bs4 import BeautifulSoup

url_string = "http://www.watermark.org/message/44000"

try:
	response_code = urllib2.urlopen(url_string).getcode()
	if(response_code != 200):
		print "Not 200"
	else:
		print response_code
except:
	print "Not connected"