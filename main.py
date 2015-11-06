#This script is designed to scrape Encyclopaedia Denhac for the current button to pop values
#Logic
##Get the web page at http://denhac.org/wiki/index.php?title=Soda_Machine 
##Parse it for the key value pair of button:sodaType
##Export it as JSON to a flat file with specified path

import urllib2,pprint
from bs4 import BeautifulSoup

def main():
	wiki = "http://denhac.org/wiki/index.php?title=Soda_Machine"
	page = urllib2.urlopen(wiki)
	soup = BeautifulSoup(page)
	table = soup.find("table", { "class" : "wikitable" })
	#We have the table now.


if __name__ == '__main__':
	main()