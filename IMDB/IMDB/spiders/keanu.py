import scrapy
#from web_scraper.items import WebScraperItem
#from scrapy.loader import ItemLoader
class ScrapySpider(scrapy.Spider):
	name = "websites"
	start_urls = ['https://www.climatestotravel.com/climate/south-africa']
	def parse(self,response):
		for website in response.xpath("//div[@class='div-tabella']"):
			print(website)
			yield{
                'movie_name': website
            }
			#l = ItemLoader(item=WebScraperItem(), selector=website)
			#l.add_xpath('website_tables',"./table")
			#yield l.load_item()