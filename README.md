# Sentimental_Analysis

Twitter Sentiment Analysis Challenge for Learn Python for Data Science #2 by @Sirajology on Youtube

##Overview

This is the code for the Twitter Sentiment Analyzer challenge for 'Learn Python for Data Science #2' by @Sirajology on YouTube. The code uses the tweepy library to access the Twitter API and the TextBlob library to perform Sentiment Analysis on each Tweet. We'll be able to see how positive or negative each tweet is about whatever topic we choose.

##Dependencies

tweepy (http://www.tweepy.org/)
textblob (https://textblob.readthedocs.io/en/dev/)
Install missing dependencies using pip

##Usage

Once you have your dependencies installed via pip, run the script in terminal via

python Sentimental_Analysis.py

Printed out each tweet and saved each Tweet to a CSV file with an associated index of 'Tweet' and 'Sensation'. 
Created Bag of Words to create traing set and test set in 'Bag_Of_Word.py'.

##The Callenge is was:
The label should be either 'Positive' or 'Negative'. You can define the sentiment polarity threshold yourself, whatever you think constitutes a tweet being positive/negative. Push your code repository to github then post it in the comments. I'll give the winner a shoutout a week from now!

##How Challenge is handled:
While checking sentiment of tweet condition of if else is added so that before writing to csv, it will chnage the replace the value of sentiment by Positive, Negative and Neutral.

##Credits

Some part of the code is by Siraj Raval, but Bag of word creation is mine.
