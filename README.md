# Spider-TurkishStocks
Scraping BigPara and Bloomberg websites in order to crawl Turkish stock market data daily.
BigPara directory scrapes: http://bigpara.hurriyet.com.tr/borsa/
Portfolio directory scrapes: https://www.bloomberght.com/borsa/

in order to run scraping spiders first delete stoklar.json files otherwise new data overwrite onto the old one.
util directories are for cleaning scraped data.
app.py inside the bigpara is a small Flask application displaying scraped data, run command "python app.py" inside the directory.
