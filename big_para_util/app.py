# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 18:32:21 2018

@author: Zeynep CANKARA

Run spider from flask
"""
from flask import Flask, render_template, request
import json_to_csv

app = Flask(__name__)
#take the list
stock_list = json_to_csv.return_stocks()
#name of the stock
title_list = list()
for stock in stock_list:
    title_list.append(stock.return_title())


@app.route("/")
def index():
    return render_template("index.html", names = title_list)


@app.route("/data", methods=["POST"])
def data():
    name = request.form.get("name")
    for stock in stock_list:
        print(stock.return_title())
        if stock.return_title() == name:
            price = stock.return_price()
            volume_lot = stock.return_lot()
            volume_tl = stock.return_tl()
            rateChange = stock.return_change()
            yesterday = stock.return_yesterday()
            return render_template("data.html", name=name, price = price, volume_lot=volume_lot,  volume_tl= volume_tl, rateChange=rateChange, yesterday=yesterday )
    return render_template("error.html")


if __name__ == '__main__':
    app.run(debug=True)
