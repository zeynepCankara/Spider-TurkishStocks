# Turkish Stock Crawler :spider:
Scraping BigPara and Bloomberg websites in order to crawl Turkish stock market data daily.

- BigPara directory scrapes: http://bigpara.hurriyet.com.tr/borsa/
- Portfolio directory scrapes: https://www.bloomberght.com/borsa/

In order to run scraping spiders first delete "stoklar.json" files otherwise new data will overwrite the old one.
- Note: Util directories are for cleaning scraped data.
- Inside "App.py" within bigpara directory there is a small Flask application displaying scraped data
- Run command "python app.py" inside the directory to view the scraped data.
