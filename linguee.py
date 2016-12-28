# linguee definition && examples scraper

import sys
try:
	from urllib.request import urlopen
except ImportError:
	from urllib2 import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup

whatWord = quote(sys.argv[1])
lingueeLink = "http://www.linguee.com/english-french/search?source=auto&query=" + whatWord
page = urlopen(lingueeLink)
initial = BeautifulSoup(page, "html.parser")

def define():
	definition = initial.find('a', class_="dictLink featured")

	if definition is not None:
		definition = initial.find('a', class_="dictLink featured").get_text()
	else:
		definition = "Word not found"
	return definition

def genExample():

	example = initial.find('table', class_="result_table")

	# left[0] in french ~ right[0] in english

	left = [] # the french sentence array
	right = [] # the corresponding english sentence array

	for row in example.findAll("tr"):
		lefty = row.find('td', class_="sentence left")
		link1 = (lefty.find('div', class_="source_url_spacer")).get_text()
		righty = row.find('td', class_="sentence right2")
		link2 = (righty.find('div', class_="source_url_spacer")).get_text()
		left.append((lefty.get_text()).replace("\n", " ").replace(link1,"").replace("\r", ""))
		right.append((righty.get_text()).replace("\n", " ").replace(link2,"").replace("\r", ""))

	sendExample = [left[0], right[0]] # send random examples? need to repurpose for context-based searches later.

	return sendExample

print ("DEFINITION: " + define())
print ("")
print ("EXAMPLE:")
print ("")
token = genExample()
print ("FRENCH: " + token[0])
print ("")
print ("ENGLISH: " + token[1])