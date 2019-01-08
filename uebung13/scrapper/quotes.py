from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
import random

marriage_url = "http://quotes.yourdictionary.com/theme/marriage/"
marriage_html = urlopen(marriage_url).read()
marriage_soup = BeautifulSoup(marriage_html)

quotes = marriage_soup.findAll("p", limit=5, attrs={"class" : "quoteContent"})

five_quotes = random.sample(quotes, 5)
for quote in five_quotes:
    print(quote.text + "\n")

