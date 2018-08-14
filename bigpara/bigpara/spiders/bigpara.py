# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 15:44:38 2018

@author: Zeynep CANKARA 

Scraping the Big Para

run this in the spider directory of the project
scrapy crawl bigpara -o stoklar.json

titles = response.css("a[href*='/borsa/hisse-fiyatlari']::text").extract() (hisse adlarını döndürüyor)
time = response.css("#son_veri_zamani::text").extract_first() (verinin geldiği son zamanı)
content = response.css("div[class*='tBody ui-unsortable']")
price = içerik.css("li[id*='h_td_fiyat_id']::text").extract() (list of açılış price)
volume_lot = içerik.css("li[id*='h_td_hacimlot_id']::text").extract() (lot hacmi)
rate = içerik.css("li[id*='h_td_yuzde_id']::text").extract() 
yesterday = içerik.css("li[id*='h_td_dunkapanis_id']::text").extract() 
volume_tl = içerik.css("li[id*='h_td_hacimtl_id']::text").extract() 
"""

import scrapy

class BigParaSpider(scrapy.Spider):
    name = "bigpara"
    allowed_domains = ['bigpara.hurriyet.com.tr']
    start_urls = [
        'http://bigpara.hurriyet.com.tr/borsa/canli-borsa/'
    ]

    def parse(self, response):
        for stoklar in response.css("div[class*='tBody ui-unsortable']"):
            yield {
                'time': response.css("#son_veri_zamani::text").extract_first(),
                'titles': stoklar.css("a[href*='/borsa/hisse-fiyatlari']::text").extract(),
                'price': stoklar.css("li[id*='h_td_fiyat_id']::text").extract(),
                'rateChange': stoklar.css("li[id*='h_td_yuzde_id']::text").extract(),
                'volume_lot': stoklar.css("li[id*='h_td_hacimlot_id']::text").extract(),
                'volume_tl': stoklar.css("li[id*='h_td_hacimtl_id']::text").extract(),
                'yesterday': stoklar.css("li[id*='h_td_dunkapanis_id']::text").extract()
            }