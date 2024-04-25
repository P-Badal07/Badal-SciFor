# -*- coding: utf-8 -*-
"""EMAIL SPAM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fpCXYL7Qy4rEWyvlAoDUkOwRtkWvIBBi
"""

import numpy as np
import pandas as pd

import pandas as pd
# List of possible encodings to try
encodings = ['utf-8', 'latin1', 'ISO-8859-1', 'cp1252']

file_path = 'spam.csv' # Change this to the path of your CSV file

# Attempt to read the CSV file with different encodings
for encoding in encodings:
  try:
    df = pd. read_csv (file_path, encoding=encoding)
    print (f"File successfully read with encoding: {encoding}")
    break #Stop the Loop if successful
  except UnicodeDecodeError:
    print (f"Failed to read with encoding: {encoding}")
    continue # Try the next encoding

# If the Loop completes without success, df will not be defined
if 'df' in locals():
  print("CSV file has been successfully loaded.")
else:
  print("All encoding attempts failed. Unable to read the CSV file.")

df.sample(5)

df.shape

#data cleaning

df.info()

# drop Last 3 cols
df.drop (columns=['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'],inplace=True)

df.sample (5)

#renaming the cols
df.rename(columns={'v1' : 'target', 'v2': 'text'},inplace=True)
df.sample (5)

from sklearn.preprocessing import LabelEncoder
encoder= LabelEncoder ()

df['target'] = encoder.fit_transform(df['target'])

df.head()

# missing values
df.isnull().sum()

# check for duplicate values
df. duplicated ().sum()

# remove duplicates
df = df.drop_duplicates (keep='first')

df.duplicated().sum()

df.shape

#EDA

df.head()

df['target'].value_counts()

import matplotlib.pyplot as plt
plt.pie(df['target'].value_counts(), labels=['ham', 'spam' ], autopct="%0.2f")
plt.show()

import nltk
!pip install nltk

df['num_characters'] = df [ 'text'].apply(len) #number of char
df.head()

nltk.download('punkt')

# number pf words
df['num_words'] = df['text'].apply(lambda x:len (nltk.word_tokenize(x))) #words count
df.head()

df['num_sentences'] = df['text'].apply(lambda x:len (nltk. sent_tokenize(x)))#sentence
df.head()

df[['num_characters', 'num_words', 'num_sentences']].describe()

# targeting spam
df [df [ 'target'] == 1] [['num_characters', 'num_words', 'num_sentences']].describe()

import seaborn as sns
plt.figure (figsize=(12,6))
sns.histplot(df[df['target']== 0]['num_characters'])
sns.histplot(df[df['target']== 1]['num_characters'], color='red')

plt. figure(figsize=(12,6))
sns.histplot (df[df['target'] == 0]['num_words'])
sns.histplot (df[df['target'] == 1]['num_words'], color='red')

sns.pairplot (df, hue='target')

sns. heatmap(df.corr(),annot=True)

# data preprocessing

nltk.download ('stopwords')

import string
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def transform_text(text):
  text = text.lower()

  text = nltk.word_tokenize(text)
  y = []
  for i in text:
    if i.isalnum():
      y.append(i)


  text = y[:]
  y.clear()


  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation:
      y.append(i)

  text = y[:]
  y.clear()


  for i in text:
    y.append(ps.stem(i))


  return" ".join(y)

transform_text('HI Somu MY sely Ak?!')

from nltk.corpus import stopwords

nltk.download('stopwords')

stopwords.words('english')

ps.stem('dancing')

df['transform_text'] = df['text'].apply(transform_text)

df#

#word cloud

from wordcloud import WordCloud
wc = WordCloud(width = 600,height = 700,min_font_size = 10,background_color = 'yellow')

spam_wc = wc.generate(df[df['target'] == 1]['transform_text'].str.cat(sep = ' '))

plt.imshow(spam_wc)

spam_corpus = []
for msg in df[df['target']==0]['transform_text'].tolist():
  for word in msg.split():
    spam_corpus.append(word)

len(spam_corpus)

from collections import Counter
pd.DataFrame(Counter(spam_corpus).most_common(50))

#model building

from sklearn. feature_extraction.text import CountVectorizer , TfidfVectorizer
cv = CountVectorizer()
tfidf = TfidfVectorizer()

x= tfidf.fit_transform(df['transform_text']). toarray()
x.shape

y = df['target'].values

y

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y , test_size = 0.2 , random_state = 2 )

from sklearn.naive_bayes import GaussianNB, MultinomialNB,BernoulliNB
from sklearn.metrics import accuracy_score ,confusion_matrix, precision_score

gnb = GaussianNB()
mnb = MultinomialNB()
bnb = BernoulliNB()

gnb.fit(x_train, y_train)
y_pred1 = gnb.predict (x_test)
print (accuracy_score(y_test, y_pred1))
print (confusion_matrix(y_test, y_pred1))
print(precision_score(y_test, y_pred1))

mnb.fit (x_train, y_train)
y_pred2 = mnb.predict(x_test)
print(accuracy_score(y_test, y_pred2))
print(confusion_matrix(y_test, y_pred2))
print(precision_score(y_test, y_pred2))

bnb.fit(x_train, y_train)
y_pred3 = bnb.predict(x_test)
print(accuracy_score(y_test, y_pred3))
print(confusion_matrix(y_test, y_pred3))
print(precision_score(y_test, y_pred3))

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier , ExtraTreesClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier

import pickle
pickle.dump(tfidf,open('vectorizer.pkl','wb'))
pickle.dump(mnb,open('model.pkl','wb'))

df['transform_text'][4532]

df.sample(10)

