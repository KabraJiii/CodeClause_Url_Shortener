import pyshorteners
from pyshorteners import Shortener

url = input('Enter the url :- ')

def shortenurl(url):
    s = pyshorteners.Shortener()
    print('The Shorter Url is :- ')
    print(s.tinyurl.short(url))

shortenurl(url)