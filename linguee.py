# linguee definition && examples scraper

# TO DO (by order of importance):

# 1) support unicode for FR-EN (and, by extension, other languages)
# 2) fix example generation
# 3) accept whatWord as an argument in the terminal process / make script available for use

# to think about: better to use an API?

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
from bs4 import BeautifulSoup

whatWord = "vie"
lingueeLink = "http://www.linguee.com/english-french/search?source=auto&query=" + whatWord
page = urlopen(lingueeLink)
initial = BeautifulSoup(page, "html.parser")

definition = initial.find('a', class_="dictLink featured").string
example = initial.find('table', class_="result_table")
left = []
right = []

# not working yet; need to investigate html.

for row in example.findAll("tr"):
	lefty = row.findAll('td', class_="sentence left")
	righty = row.findAll('td', class_="sentence right2")
	left.append(lefty[0].find(text=True))
	right.append(righty[0].find(text=True))

print (definition)
print (left, right)