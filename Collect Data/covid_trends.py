#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:39:13 2020

@author: bogt
"""

# Basic imports and settings
import pandas as pd
from pytrends.request import TrendReq

import csv
import numpy
import time

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 200)
pd.set_option('display.max_colwidth', 100)
pd.set_option('display.width', None)

###############################################
###############################################

# Connected to trends API
pytrend = TrendReq(hl='en-US', tz=360)

kw_list = ['Coronavirus']
pytrend.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='CA', gprop='')

###############################################
###############################################

# Interest By Region
print('Interest by region')
df = pytrend.interest_by_region()
print(df.head(10))
df.reset_index().plot(x='geoName', y='Coronavirus', figsize=(120, 10), kind ='bar')

df.to_csv('covid_by_region.csv', sep=',')
###############################################
###############################################

# Daily search trends
print('\nDaily search trends')
df = pytrend.trending_searches(pn='canada')
print(df.head())

df.to_csv('trending.csv', sep=',')

df = pytrend.today_searches(pn='CA')
print(df.head())

df.to_csv('trending_today.csv', sep=',')
###############################################
###############################################

# Get Google Top Charts
print('\nGoogle past top charts')
df = pytrend.top_charts(2019, hl='en-US', tz=300, geo='CA')
print(df.head())

df.to_csv('top_charts.csv', sep=',')

###############################################
###############################################

# Get Google Keyword Suggestions
print('\nGoogle keyword suggestions')
keywords = pytrend.suggestions(keyword='covid')
df = pd.DataFrame(keywords)
df.drop(columns= 'mid')   # This column makes no sense
print(df.head())
df.to_csv('covid_suggestions.csv', sep=',')


dict_queries = pytrend.related_queries()
df = pd.DataFrame.from_dict(dict_queries, orient='index')
df.to_csv('covid_related_queries.csv', sep=',')
print(dict_queries.values())

dict_topics = pytrend.related_topics()
df = pd.DataFrame.from_dict(dict_topics, orient='index')
df.to_csv('covid_related_topics.csv', sep=',')
print(dict_topics.values())