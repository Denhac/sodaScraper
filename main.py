#This script is designed to scrape Encyclopaedia Denhac for the current button to pop values
#Logic
##Get the web page at http://denhac.org/wiki/index.php?title=Soda_Machine 
##Parse it for the key value pair of button:sodaType
##Export it as JSON to a flat file with specified path

import urllib2,re,sys,itertools
from bs4 import BeautifulSoup

def main():
	completeList = list()
	completeDict = dict()
	wiki = "http://denhac.org/wiki/index.php?title=Soda_Machine"
	page = urllib2.urlopen(wiki)
	soup = BeautifulSoup(page)
	table = soup.find("table", { "class" : "wikitable" })
	#We have the table now.  Just need to parse the data into a JSON type
	for row in table.findAll("tr"):
	    cells = row.findAll("td")
	    #For each "tr", assign each "td" to a variable.
	    cellsList = list(cells)
	    if len(cellsList) == int(2):
	    	cellsList
	    	for line in cellsList:
	    		line = str(line)
	    		line = line.replace("<td>","").replace("</td>","").replace("\n","")
	    		completeList.append(line)
	while len(completeList) >= 2:
		completeDict[completeList[0]] = completeList[1]
		completeList.pop(0)
		completeList.pop(0)
		

		


if __name__ == '__main__':
	main()