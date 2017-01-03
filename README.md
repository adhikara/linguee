#linguee#

This is a simple web scraper to fetch translations from [Linguee](http://www.linguee.com).

Use `pip` to install BeautifulSoup (`bs4`) in order to use this code.

#usage#

The code is set up to generate the definition and the first example from Linguee.

Use: `python linguee.py [french word]`

Because of how Linguee works, you can also try `python linguee.py [english word]` to get the French translation. It is also possible to make this code able to pull translations for any language -- you need to simply change the website queried to `www.linguee.com`. However, note that you will need to modify the code to pull other features like what language the original text is in and things like that.

#warning#

Linguee has [rules](http://www.linguee.com/english-french/page/termsAndConditions.php) about how its website is used.

This code is obviously not fetching data from Linguee's API, as it does not have one yet. It could stop working if the developers change the HTML tags, organization of the HTML output, etc.

Also, **please note** that if you send too many requests to Linguee, this will happen: "You have sent too many requests causing Linguee to block your computer" (lol: from experience).

In response to this, I am changing the translation methods to instead

1) Search through Wiktionary dumps
2) Search through Wiktionary when nothing is found in the dumps, including lookup for past participles and singulars and things like that
3) Only when these methods fail does the code look up the word in Linguee

In the future, when I get API keys, I will remove Linguee altogether and use other websites that allow up to 5000 calls per month.
