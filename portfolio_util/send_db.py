# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 20:57:08 2018

@author: Zeynep Cankara

Module for writing the data in portfolio to database in the stock app

cleaning scraped data for Yahoo finance

"""
import json
#load the stock data i
json_data=open('stoklar.json').read()
data = json.loads(json_data)

def titles():
    titles =list()
    for element in range(len(data)):
        for t in data[element]['titles']:
                if(type(t) == str):
                    titles.append(t)
    return titles

def prices():
    price = list()
    for element in range(len(data)):
        for t in data[element]['price']:
                if(type(t) == str and t != "SON"):
                    price.append(t)
    return price

def rates():
    rate = list()
    for element in range(len(data)):
        for t in data[element]['rate']:
                if(type(t) == str and t != "SON" and t!= "%"):
                    rate.append(t)
    return rate

def yesterday():
    yesterday = list()
    for element in range(len(data)):
        for t in data[element]['yesterday']:
                if(type(t) == str and t != "SON" and t!= "DÜN"):
                    yesterday.append(t)
    return yesterday

def volume_lot():
    volume_lot = list()
    for element in range(len(data)):
        for t in data[element]['volume_lot']:
                if(type(t) == str and t != "HACİM LOT" and t!= "HAC\u0130M LOT" and t != "SON"):
                    volume_lot.append(t)
    return volume_lot

def volume_tl():
    volume_tl = list()
    for element in range(len(data)):
        for t in data[element]['volume_tl']:
                if(type(t) == str and t != "HACİM TL" and t != "HAC\u0130M TL" and t != "SON"):
                    volume_tl.append(t)
    return volume_tl

title_final = list()
titles = titles()
price = prices()
volume_lot = volume_lot()
volume_tl = volume_tl()
rate = rates()
yesterday = yesterday()

#Execute in the python manage.py shell for writing into Django database Date is a model that I created for app
"""
from stocks.models import Portfolio, Date, Stock
date_09_08_2018 = Date(day = 9, month = "August", year = 2018)
date_09_08_2018.save()
for e in range(len(titles)):
    if titles[e] not in title_final:
        title_final.append(titles[e])
        s = Stock(title = str(titles[e]), price = str(price[e]), volume_lot = str(volume_lot[e]), volume_tl = str(volume_tl[e]),yesterday = str(yesterday[e]), rate = str(rate[e]), date = date_09_08_2018)
        s.save()
"""
