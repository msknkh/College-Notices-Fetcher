# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 11:37:04 2019

@author: muskan
"""

import requests
import pandas as pd
import sendgrid
from sendgrid.helpers.mail import *
from bs4 import BeautifulSoup as soup

resp =  requests.get("https://imsnsit.org/imsnsit/notifications.php");

resp_soup = soup(resp.content,'lxml')

df = pd.DataFrame(columns =['Date','Heading','Link'])
trs = resp_soup.findAll('tr')
l = len(trs)
j=0

for i in range(3,l-2,2):
    tds = trs[i].findAll('td')
    date=tds[0].text.strip()
    heading = tds[1].text.strip()
    href=tds[1].a['href']
    df.loc[j]=[date,heading,href]
    j+=1
    
    
df.to_csv('database.csv')    