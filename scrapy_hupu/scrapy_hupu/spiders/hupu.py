import scrapy
from scrapy_hupu.items import ScrapyHupuItem

class HupuSpider(scrapy.Spider):
    name = 'hupu'
    allowed_domains = ['bbs.hupu.com']
    start_urls = ['https://bbs.hupu.com/lakers']
    base_url =  'https://bbs.hupu.com/lakers-'
    page = 1
    def parse(self, response):
        #//li[@class ="bbs-sl-web-post-body"]//div[@ class ="post-title"] / a / text()

        li_list = response.xpath('//li[@class="bbs-sl-web-post-body"]')
        #div[ @class ="post-title"] / a / text()
        for li in li_list:
            title = li.xpath('.//div[@class="post-title"]/a/text()').extract_first()
            author = li.xpath('.//div[@class="post-auth"]/a/text()').extract_first()
            time = li.xpath('.//div[@class="post-time"]/text()').extract_first()
            hupuu = ScrapyHupuItem(title=title,author=author,time=time)
            yield hupuu

        if self.page < 10:
            self.page += 1
            url = self.base_url +str(self.page)

            yield scrapy.Request(url = url ,callback=self.parse)
