import scrapy

class Movies(scrapy.Spider):
    name = 'movies'
    start_urls = ["https://www.imdb.com/search/title/?genres=comedy&genres=Romance&explore=title_type,genres&ref_=adv_explore_rhs"]


    def parse(self,response):
        for movies in response.xpath('//div[@class="lister-item-content"]'):
            yield{
                 'Movie_Name': movies.xpath('.//h3[@class="lister-item-header"]/a/text()').extract_first(),
                 'Genre' : response.xpath('.//p[1]/span[@class="genre"]/text()').extract(),
                 'Runtime' : response.xpath('.//p/span[@class="runtime"]/text()').extract_first(),
                 'Year' : response.xpath('.//h3[@class="lister-item-header"]/span[@class="lister-item-year text-muted unbold"]/text()').extract_first(),
                 'Synopsis' : response.xpath('.//p[@class="text-muted"]/text()').extract_first(),
                 'Votes' : response.xpath('.//a[@class="lister-page-next next-page"]/@href').extract_first(),
                 'Gross Amount' : response.xpath('.//a[@class="lister-page-next next-page"]/@href').extract_first(),
                 'Rating' : response.xpath('.//a[@class="lister-page-next next-page"]/@href').extract_first(),
                 'Metascore' : response.xpath('.//a[@class="lister-page-next next-page"]/@href').extract_first()
            }

        # next_page = response.xpath('//a[@class="lister-page-next next-page"]/@href').extract_first()
        # if next_page is not None:
        #     next_page_link = response.urljoin(next_page)
        #     yield scrapy.Request(url=next_page_link,callback=self.parse)
            
           

