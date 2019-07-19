###### IMPORT PANDAS AND DOWNLOAD NLTK AND CORPUS
import pandas as pd
import numpy as np
import csv
from pandas import read_csv
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer  
nltk.download()


###Initiate and isntance of object SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

#### Fill all null values by a neutral statemnt
df_text['merchant_first_reply'] =  df_text['merchant_first_reply'].fillna(value = " Hi hello")

#### Apply the method polarity scores
df_text['mfr_score'] = df_text['merchant_first_reply'].apply(lambda x : sid.polarity_scores(x))

#### Get positive values from the dict item
df_text['mfr_pos'] = df_text['mfr_score'].apply(lambda x : x.get("pos"))
