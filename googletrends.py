from pytrends.request import TrendReq
import matplotlib
import pandas as pd
import csv

pytrends = TrendReq(hl='en-US, tz=360')
k_list = ['Wizkid']
pytrends.build_payload(k_list, cat=0, timeframe='today 3-m', geo='US', gprop='')

print(pytrends.related_topics())