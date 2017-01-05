import urllib2
from bs4 import BeautifulSoup
import xlwt

# EXCEL PART
wmdb_book = xlwt.Workbook(encoding="utf-8")
sheet1 = wmdb_book.add_sheet("Sheet1")

sheet1.write(0, 0, "Sermon")
sheet1.write(0, 1, "Date")

# URL PART
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
			title_string = str(title_string)
		if(title_string != ""):
			date_created = soup.findAll('span', {'class': 'date'})[0].contents[0]
			date_created = str(date_created)
			#sheet1.write(1, 0, title_string)
			#sheet1.write(1, 1, date_created)
			
except:
	print "Not connected"

wmdb_book.save('db.xls') # Close the Excel Workbook