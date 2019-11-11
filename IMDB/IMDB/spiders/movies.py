import scrapy

class Movies(scrapy.Spider):
    name = 'movies'
    start_urls = ["https://www.imdb.com/search/title/?genres=comedy&genres=Romance&explore=title_type,genres&ref_=adv_explore_rhs"]


    def parse(self,response):
        for movies in response.xpath('//div[@class="lister-item-content"]'):
            yield{
                 'Movie_Name': movies.xpath('.//h3[@class="lister-item-header"]/a/text()').extract_first(),
                 'Genre' : movies.xpath('.//p[1]/span[@class="genre"]/text()').extract_first(),
                 'Runtime' : movies.xpath('.//p/span[@class="runtime"]/text()').extract_first(),
                 'Year' : movies.xpath('.//h3[@class="lister-item-header"]/span[@class = "lister-item-year text-muted unbold"]/text()').extract_first(),
                 'Synopsis' : movies.xpath('.//p[@class="text-muted"]/text()').extract_first(),
                 'Votes' : movies.xpath('.//a[@class="lister-page-next next-page"]/@href').extract_first(),
                 'Gross Amount' : movies.xpath('.//a[@class="lister-page-next next-page"]/@href').extract_first(),
                 'Rating' : movies.xpath('.//a[@class="lister-page-next next-page"]/@href').extract_first(),
                 'Metascore' : movies.xpath('.//a[@class="lister-page-next next-page"]/@href').extract_first()
            }

        # next_page = response.xpath('//a[@class="lister-page-next next-page"]/@href').extract_first()
        # if next_page is not None:
        #     next_page_link = response.urljoin(next_page)
        #     yield scrapy.Request(url=next_page_link,callback=self.parse)
            
           

