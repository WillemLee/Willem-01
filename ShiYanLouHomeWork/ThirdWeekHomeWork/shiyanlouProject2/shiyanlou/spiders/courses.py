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
        for course in response.css('li[class="col-12"]'):
             yield ShiyanlouItem({
                  'name':course.css('div[class="d-inline-block mb-1"] a::text').re_first('[^\w]*(\w*)[^\w]*'),
                 # 'update_time':response.xpath('div[@class="f6 text-gray mt-2"]/relative-time/@datetime').extract_first()
                 'update_time' :course.css('div[class="f6 text-gray mt-2"] relative-time::attr(datetime)').extract_first(),
                   
              authenticity_token = response.xpath('//div[@id="login"]//input[@name="authenticity_token"/@value"]').extract_first()

               self.logger.info(csrf_token)
               return scrapy.FormRequest.from_response(
                          response,
                          formdata={
                          'authenticity_token':authenticity_token,
                          'login_field':'liwenliang_9527@163.com',
                           'password':'lwl15835122809',
                   
                           },
                    callback = self.after_login
                )
               })

    def after_login(self,response):

        return [scrapy.Request(
            url = response.xpath('//div[@class="d-inline-block"]/h3/a/@href').extract_first(),
            yield response.follow(url,callback=self.parse)
            )]

    def parse_after_login(self,response):

        return {
                'commits' = response.xpath('//li[@class="commits"]/a/span/text()').extract_first(),
                'branches' = response.xpath('//li//a[@text="branch"]/span/text()').extract_first(),
                'releases' = response.xpath('//li//a[@text="releases"]/span/text()').extract_first(),
                }
