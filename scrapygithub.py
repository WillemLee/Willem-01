# usr/bin/env python3

import scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):

    name = 'shiyanlou-courses'

    @property
    def start_urls(self):

        url_tmp1 = 'https://github.com/shiyanlou?page={}&tab=repositories'

        return (url_tmp1.format(i) for i in)
