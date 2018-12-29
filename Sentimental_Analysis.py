# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 15:21:49 2018

@author: kisku
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 01:48:17 2018

@author: kisku
"""
import tweepy
from textblob import TextBlob
import csv
import pandas as pd

consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
number_of_tweets=200
#Open/create a file to append data to
csvFile = open('result.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

public_tweets = api.search('Subject')

#dataframe = pd.DataFrame
threshold = 0

for tweet in public_tweets:
    print(tweet.text)
    analysis =TextBlob(tweet.text)
    print(analysis)
    print(analysis.polarity)
    If analysis.polarity > threshold:
        analysis.polarity = 'Positive'
    elif analysis.polarity < threshold:
        analysis.polarity = 'Negative'
    else:
        analysis.polarity = 'Neutral'
    csvWriter.writerow([tweet.text.encode('utf-8'),analysis.polarity])
    
csvFile.close()

# Labeling the dataset by indexing.
dataset = pd.read_csv('result.csv', index_col='Tweet', header=0, names=['Tweet','Sensation'])
dataset.to_csv('Training_Sheet.csv')
dataset = pd.read_csv('Training_Sheet.csv')
