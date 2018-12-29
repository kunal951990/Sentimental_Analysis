# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 15:18:18 2018

@author: kisku
"""

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Training_Sheet.csv')

corpus = []
for i in range(0, 14):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Tweet'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

"""Now we have our Training set in form of X and Y"""