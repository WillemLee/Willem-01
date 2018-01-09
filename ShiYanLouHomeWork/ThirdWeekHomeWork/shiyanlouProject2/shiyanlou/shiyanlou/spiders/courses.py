# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import ShiyanlouItem

class CoursesSpider(scrapy.Spider):
    name = 'courses'
    @property
    def start_urls(self):
        start_urls = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (start_urls.format(i) for i in range(1,5))
    
    def parse(self, response):
        for course in response.css('li.public'):
            item = ShiyanlouItem()
            item['name']=course.css('div[class="d-inline-block mb-1"] a::text').re_first('[^\w]*(\w*)[^\w]*')
            # 'update_time':response.xpath('div[@class="f6 text-gray mt-2"]/relative-time/@datetime').extract_first()
            item['update_time']=course.css('div[class="f6 text-gray mt-2"] relative-time::attr(datetime)').extract_first()
            url = response.urljoin(course.xpath('.//a/@href').extract_first())
            request = scrapy.Request(url,callback=self.parse_repo)
            request.meta['item'] = item
            yield request

    def parse_repo(self,response):
        item = response.meta['item']
        for num_li in response.css('ul.numbers-summary li'):
            content_text = num_li.xpath('.//a/text()').re_first('\n\s*(.*)\n')
            num_text = num_li.xpath('.//span[@class="num text-emphasized"]/text()').re_first('\n\s*(.*)\n')
            if content_text and num_text:
                num_text = num_text.replace(',','')
                if content_text in ('commit','commits'):
                    item['commits']  = int(num_text)
                elif content_text in('branch','branches'):
                    item['branches'] = int(num_text)
                elif content_text in('release','releases'):
                    item['releases'] = int(num_text)
        yield item
