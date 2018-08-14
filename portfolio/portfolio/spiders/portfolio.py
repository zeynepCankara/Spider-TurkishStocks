# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 09:02:25 2018

@author: Zeynep CANKARA

Scraping Bloomberg website for creating a Personal Portfolio app

SCRAPY SHELL COMMANDS
içerik = response.css("table[class*='table table-striped mar0']")
stocks = içerik.css("tr")
stock = stocks.css("td")
titles = stock.css("a::text").extract() #gives all the titles in a list
values = stock.css("td::text").extract() #gives all of the values 
next_page = response.css("ul[class*='pagination']")
follow_page = next_page.css('li a::attr(href)').extract_first()
follow_page = next_page.css('li a::text').extract()

scrapy crawl bloomberg -o stoklar.json 
"""

import scrapy

class BloomBergSpider(scrapy.Spider):
    name = "bloomberg"
    allowed_domains = ['bloomberght.com']
    start_urls = [
        'https://www.bloomberght.com/borsa/hisseler/A',
        'https://www.bloomberght.com/borsa/hisseler/B',
        'https://www.bloomberght.com/borsa/hisseler/C',
        'https://www.bloomberght.com/borsa/hisseler/D',
        'https://www.bloomberght.com/borsa/hisseler/E',
        'https://www.bloomberght.com/borsa/hisseler/F',
        'https://www.bloomberght.com/borsa/hisseler/G',
        'https://www.bloomberght.com/borsa/hisseler/H',
        'https://www.bloomberght.com/borsa/hisseler/I',
        'https://www.bloomberght.com/borsa/hisseler/J',
        'https://www.bloomberght.com/borsa/hisseler/K',
        'https://www.bloomberght.com/borsa/hisseler/L',
        'https://www.bloomberght.com/borsa/hisseler/M',
        'https://www.bloomberght.com/borsa/hisseler/N',
        'https://www.bloomberght.com/borsa/hisseler/O',
        'https://www.bloomberght.com/borsa/hisseler/P',
        'https://www.bloomberght.com/borsa/hisseler/R',
        'https://www.bloomberght.com/borsa/hisseler/S',
        'https://www.bloomberght.com/borsa/hisseler/T',
        'https://www.bloomberght.com/borsa/hisseler/U',
        'https://www.bloomberght.com/borsa/hisseler/V',
        'https://www.bloomberght.com/borsa/hisseler/Y',
        'https://www.bloomberght.com/borsa/hisseler/Z'
        
    ]


    def parse(self, response):
        içerik = response.css("table[class*='table table-striped mar0']")
        stocks = içerik.css("tr")
        stock = stocks.css("td")
        values = stock.css("td::text").extract()
        
        empty_list = list()
        price_list = list()
        yesterday_list = list()
        rate_list = list()
        high_list = list()
        low_list = list()
        volume_lot = list()
        volume_tl = list()
        
        
        count = 1
        for element in values:
            if(count % 8 == 1):
                empty_list.append(element)
            if(count % 8 == 2):
                price_list.append(element)
            if(count % 8 == 3):
                yesterday_list.append(element)
            if(count % 8 == 4):
                rate_list.append(element)
            if(count % 8 == 5):
                high_list.append(element)
            if(count % 8 == 6):
                low_list.append(element)
            if(count % 8 == 7):
                volume_lot.append(element)
            if(count % 8 == 0):
                volume_tl.append(element)
            count += 1
        
        a = dict()
        
        a['empty'] = empty_list
        a['price'] = price_list
        a['vol_tl'] = volume_tl
        a['vol_lot'] = volume_lot 
        a['high'] = high_list 
        a['low'] = low_list
        a['yesterday'] = yesterday_list
        a['rate'] = rate_list
        
        yield {
                'titles': stock.css("a::text").extract(),
                'empty': empty_list,
                'price': price_list,
                'yesterday': yesterday_list,
                'rate': rate_list,
                'high':high_list ,
                'low': low_list,
                'volume_lot':volume_lot ,
                'volume_tl':volume_tl
                }
    
        follow_page = response.css("ul[class*='pagination']")
        next_page = follow_page.css('li a::attr(href)')
        for href in next_page:
             yield response.follow(href, self.parse)