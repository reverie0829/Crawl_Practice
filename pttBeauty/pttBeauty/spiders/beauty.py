import scrapy
from pttBeauty.items import PttbeautyItem

class BeautySpider(scrapy.Spider):
    name = 'beauty'
    allowed_domains = ['ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Beauty/index.html']
    #next_url_front = ['https://www.ptt.cc']

    def parse(self, response):
        #提取所有節點列表
        nood_list = response.xpath('//*[@id="main-container"]/div[2]/div')
        #print(len(nood_list))
        


        for node in nood_list:

            item = PttbeautyItem()

            item['title'] = node.xpath('./div[2]/a/text()').extract_first()

            item['address'] = node.xpath('./div[2]/a/@href').extract_first()

            item['date'] = node.xpath('./div[3]/div[3]/text()').extract_first()

            item['author'] = node.xpath('.//div[1]/text()').extract_first()

            item['hot'] = node.xpath('./div[1]/span/text()').extract_first()

            yield item


        #模擬翻頁
        part_url = response.xpath('//*[@id="action-bar-container"]/div/div[2]/a[2]/@href').extract_first()
        #print(part_url)

        #判斷終止條件
        if part_url != None:
            next_url_front = 'https://www.ptt.cc'
            next_url = next_url_front + part_url
            yield scrapy.Request(
                url=next_url,
                callback=self.parse
            )
