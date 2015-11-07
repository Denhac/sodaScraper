#This script is designed to scrape Encyclopaedia Denhac for the current button to pop values
#Logic
##Get the web page at http://denhac.org/wiki/index.php?title=Soda_Machine 
##Parse it for the key value pair of button:sodaType
##Export it as JSON to a flat file with specified path

import urllib2,json
from bs4 import BeautifulSoup

def main():
	#Variables
	completeList = list()
	completeDict = dict()
	tempTestingFile = "testOut.json"
	remoteURL = "http://denhac.org/wiki/index.php?title=Soda_Machine"
	#Obtaining the data from the wiki
	page = urllib2.urlopen(remoteURL)
	soup = BeautifulSoup(page)
	#Get the table out of the raw HTML
	table = soup.find("table", { "class" : "wikitable" })
	#We have the table now.  Just need to parse the data into a JSON type
	for row in table.findAll("tr"):
	    cells = row.findAll("td")
	    cellsList = list(cells)
	    if len(cellsList) == int(2):
	    	cellsList
	    	#For each line in the file, remove <td> and </td> and \n with nothing.  Move each row into a list element.
	    	for line in cellsList:
	    		line = str(line)
	    		line = line.replace("<td>","").replace("</td>","").replace("\n","")
	    		completeList.append(line)
	#Turn the list into a dictionary
	while len(completeList) >= 2:
		completeDict[completeList[0]] = completeList[1]
		completeList.pop(0)
		completeList.pop(0)
	#Turn the dict into JSON
	sodaTableInJSON = json.dumps(completeDict, ensure_ascii=False)
	#Write the JSON object to a file.

	json_str = json.dumps(sodaTableInJSON)
	with open(tempTestingFile,"w") as outFile:
		outFile.write(sodaTableInJSON)

if __name__ == '__main__':
	main()