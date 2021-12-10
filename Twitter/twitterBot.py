# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:16:02 2021

@author: LENOVO
"""

import tweepy
import time
from keys import *
import requests
from lxml import html

#create twitter api object
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#time in full 
time = time.ctime()

#quote
page = requests.get("https://www.quotes.net/")
tree = html.fromstring(page.content)
quote1 = tree.xpath('//*[@id="featured-quote-int"]/blockquote[2]/a/text()')
quote2 = tree.xpath('//*[@id="featured-quote-int"]/blockquote[3]/a/text()')
quote3 = tree.xpath('//*[@id="featured-quote-int"]/blockquote[7]/a/text()')

if len(str(quote1)) > 140:
    quote1 = quote2
    if len(str(quote2)) > 140:
        quote1 = quote3

quote_final =  str(quote1).strip('[]')
print (len(quote_final))

#wiki page
current_url = requests.get("https://en.wikipedia.org/wiki/Special:Random").url

tweet_string = (str(time) +'\n\n' + quote_final + '\n\n'+ current_url )
print (tweet_string)

#UNCOMMENT when twitterBot app has been unsuspended
# && setup windows task scheduler to run this once a day
api.update_status(tweet_string)
