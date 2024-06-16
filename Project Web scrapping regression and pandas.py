#!/usr/bin/env python
# coding: utf-8

# In[12]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

url = 'http://analytictech.com/mb021/mlk.htm'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

mlkj_speech = soup.find_all('p')

speech_command = [p.text for p in mlkj_speech] #method to combined paragraph, first wr check the type og mlkj speech it turns out to be elements now speech is come together but still sperated by , and now further check it shows it is list now

string_speech = ' ' .join(speech_command)

string_speech_clean = string_speech.replace('\r\n',' ')

speech_no_punct = re.sub(r'[^\w\s]', '', string_speech_clean) #remove puntuation and extraa characters

speech_lower = speech_no_punct.lower() # lower case all para

speech_broken_out = re.split(r'\s+', speech_lower) #split each word

df = pd.DataFrame(speech_broken_out).value_counts()
df.to_csv(r'C:\Users\mussa\OneDrive\Documents\python Learning\web scraping\mlkj_speech_counts.csv', header = ['Counts'], index_label = 'Word')


# In[23]:





# In[19]:





# In[21]:





# In[ ]:




