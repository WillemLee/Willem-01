# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import ShiyanlouItem

class CoursesSpider(scrapy.Spider):
    name = 'courses'
    def parse(self, response):
        for course in response.css('li[class="col-12 d-block width-full py-4 border-bottom public source"]'):
             yield ShiyanlouItem({
                  'name':course.css('div[class="d-inline-block mb-1"] a::text').re_first('[^\w]*(\w*)[^\w]*'),
                 # 'update_time':response.xpath('div[@class="f6 text-gray mt-2"]/relative-time/@datetime').extract_first()
                 'update_time' :course.css('div[class="f6 text-gray mt-2"] relative-time::attr(datetime)').extract_first()
                                })
    @property
    def start_urls(self):
        start_urls = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (start_urls.format(i) for i in range(1,5))

