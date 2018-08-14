# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 18:51:01 2018

@author: Zeynep CANKARA

Module for reading the json response and writing into a csv file
"""
"""
    Import the libraries
"""
import os
import json
import datetime
#load the stock data i
json_data=open('stoklar.json').read()
data = json.loads(json_data)
print(data)


#get the current date
now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day

class Stock:
    """ Keeping track of the stocks later added to the database
    """
    def __init__(self, title, price, volume_lot, volume_tl, yesterday, rate):
        self.title = title;
        self.price = price;
        self.volume_lot = volume_lot;
        self.volume_tl = volume_tl;
        self.yesterday = yesterday;
        self.rate =  rate;


    def print_info(self):
        print("Title: %s"%(self.title) );
        print("Price: %s"%(self.price));
        print("Volume_lot: %s"%(self.volume_lot));
        print("Volume_tl: %s"%(self.volume_tl));
        print("Yesterday's Price: %s"%(self.yesterday));
        print("Rate of Change: %s"%(self.rate));

    def return_title(self):
        return str(self.title)

    def  return_price(self):
        return self.price

    def return_yesterday(self):
        return self.yesterday

    def return_change(self):
        return self.rate

    def return_lot(self):
        return self.volume_lot

    def return_tl(self):
        return self.volume_tl

    def return_yesterday(self):
        return self.yesterday


    
def return_stocks():
    stok_list = list()
    for element in range(len(data[0]['titles'])):
        s = Stock(data[0]['titles'][element], data[0]['price'][element], data[0]['volume_lot'][element], data[0]['volume_tl'][element],data[0]['yesterday'][element], data[0]['rateChange'][element])
        stok_list.append(s)
        for element in stok_list:
            print(element.print_info())
    return stok_list

#for django
#s = Stock(title = str(data[0]['titles'][element]), price = str(data[0]['price'][element]), volume_lot = str(data[0]['volume_lot'][element]), volume_tl = str(data[0]['volume_tl'][element]),yesterday = str(data[0]['yesterday'][element]), rate = str(data[0]['rateChange'][element]), date = date_30_07_2018)
