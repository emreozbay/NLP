import scrapy
import re
from scrapy.selector import Selector
from scrapy import Request
from .. import items


class MoviesSpider(scrapy.Spider):
    name = "movies"
    allowed_domains = ["beyazperde.com"]
    start_urls = (
        'http://www.beyazperde.com/title/tt0111161/reviews',
    )

    def parse(self, response):
		base_url = "http://www.beyazperde.com/title/tt0111161/reviews"
		print response.xpath("//*[@id='tn15content']/table[2]/tbody/tr/td[2]")
		return
        
   