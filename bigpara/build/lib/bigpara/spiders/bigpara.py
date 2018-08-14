# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 15:44:38 2018

@author: Zeynep CANKARA 

Scraping the Big Para

run this in the spider directory
scrapy crawl bigpara -o stoklar.json

titles = response.css("a[href*='/borsa/hisse-fiyatlari']::text").extract (hisse adlarını döndürüyor)
zaman = response.css("#son_veri_zamani::text").extract_first() (verinin geldiği son zamanı)
where you will run your for loop 
içerik = response.css("div[class*='tBody ui-unsortable']")
fiyat = içerik.css("li[id*='h_td_fiyat_id']::text").extract() (list of açılış price)
hacim_lot = içerik.css("li[id*='h_td_hacimlot_id']::text").extract() (lot hacmi)
yüzde = içerik.css("li[id*='h_td_yuzde_id']::text").extract() 
dün = içerik.css("li[id*='h_td_dunkapanis_id']::text").extract() 
hacim_tl = içerik.css("li[id*='h_td_hacimtl_id']::text").extract() 
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