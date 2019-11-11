import scrapy

class Movies(scrapy.Spider):
    name = 'movies'
    start_urls = ["https://www.imdb.com/search/title/?genres=comedy&genres=Romance&explore=title_type,genres&ref_=adv_explore_rhs"]
    # start_urls = ["https://www.laughfactory.com/jokes/family-jokes"]

    def parse(self,response):
        for movies in response.xpath('//div[@class="lister-item-content"]'):
        # for movies in response.xpath('//a["lister-page next-page"]/text()'):
            #print(movies)
            yield{
                #  'movie_name': movies#.xpath('.//div[@class="joke-text"]/p').extract_first()
                 'Movie_Name': movies.xpath('.//h3[@class="lister-item-header"]/a/text()').extract_first(),
                 'Genre' : response.xpath('//a[@class="lister-page-next next-page"]/@href').extract_first(),
                 'Runtime' : response.xpath('//a[@class="lister-page-next next-page"]/@href').extract_first(),
                 'Year' : response.xpath('//a[@class="lister-page-next next-page"]/@href').extract_first(),
                 'Synopsis' : response.xpath('//a[@class="lister-page-next next-page"]/@href').extract_first(),
                 'Votes' : response.xpath('//a[@class="lister-page-next next-page"]/@href').extract_first(),
                 'Gross Amount' : response.xpath('//a[@class="lister-page-next next-page"]/@href').extract_first(),
                 'Rating' : response.xpath('//a[@class="lister-page-next next-page"]/@href').extract_first(),
                 'Metascore' : response.xpath('//a[@class="lister-page-next next-page"]/@href').extract_first(),
            }

        next_page = response.xpath('//a[@class="lister-page-next next-page"]/@href').extract_first()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link,callback=self.parse)
            
           

