#linguee#

This is a simple web scraper to fetch translations from [Linguee](http://www.linguee.com).

Use `pip` to install BeautifulSoup (`bs4`) in order to use this code.

#usage#

The code is set up to generate the definition and the first example from Linguee.

Use: `python linguee.py [french word]`

#warning#

Linguee has [rules](http://www.linguee.com/english-french/page/termsAndConditions.php) about how its website is used.

This code is obviously not fetching data from Linguee's API, as it does not have one yet. So it could stop working if the developers change the HTML tags, organization of the HTML output, etc.
