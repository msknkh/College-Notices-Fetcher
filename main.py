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

def createSendStr(name,to_send):
    sendStr = "Hi " + name + ",\n\n Unread notices:\n"
    for i,notice in enumerate(to_send):
        sendStr += str(i+1) + ") "
        sendStr += "\n"+"Heading: "+to_send[i]['Heading'] + " \n"

        sendStr += "\n"+"Link: "+to_send[i]['Link'] + " \n"

        sendStr += "\n"+"date: " + to_send[i]['Date'] + " \n"
        
    return sendStr

'''def sendEmail(attenders,to_send):
    for i,row in attenders.iterrows():
        sendStr = createSendStr(row['Name'],to_send)
        sg = sendgrid.SendGridAPIClient(apikey=api_key)
        from_email = Email("muskankhandelwal369@gmail.com")
        to_email = Email(row["Email"])
        subject = "NSUT IMS Notice update"
        content = Content("text/plain", sendStr)
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())'''
        
        

def sendEmail(to_send):
        sendStr = createSendStr(Muskan,to_send)
        sg = sendgrid.SendGridAPIClient(apikey=api_key)
        from_email = Email("muskankhandelwal369@gmail.com")
        to_email = Email("muskankhandelwal369@gmail.com")
        subject = "NSUT IMS Notice update"
        content = Content("text/plain", sendStr)
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())        
        
with open('api.txt','r') as f:
    api_key = f.read()




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

db = pd.read_csv('database.csv',usecols=['Date','Heading','Link'])
headset = set(db['heading'])

to_send = []
for i,row in df.iterrows():
    
    if not row['Heading'] in headset:
        l = len(db)
        db.loc[l] = row
        to_send.append(row)    
    
db.to_csv('database.csv')   
# att = pd.read_excel('attenders.xlsx')

if len(to_send) > 0:
    #sendEmail(att,to_send)
    sendEmail(to_send)