# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import ShiyanlouItem

class CoursesSpider(scrapy.Spider):
    name = 'courses'
    start_urls = ['https://github.com/shiyanlou?page={}tab=repositories']

    def parse(self, response):
        yield,ShiyanlouItem({
              'id':response.css
              'name':response.css
              'update_time':response.xpath
            )}
        pass

    @property
    def start_urls(self):
        return (start_urls.format(i) for i in range(1,5))

