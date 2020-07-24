import scrapy
from myspider.items import MyspiderItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee']

    def parse(self, response):
        #定義對於網站的相關操作
        # with open('itcast.html', 'wb') as f:
        #     f.write(response.body)
        #獲取所有教師節點
        node_list = response.xpath('/html/body/div[14]/div/div[2]/div/div[2]/div/ul/li')
        #print(len(node_list))
        
        #遍歷教師節點
        for node in node_list:
            ##temp = {}
            item = MyspiderItem()
            #xpath方法返回的是選擇器的對象列表,extract()用於從選擇器對象提取數據
            item['name'] = node.xpath('./div/h3/text()').extract_first()
            item['title'] = node.xpath('./div/h4/text()')[0].extract()
            item['desc'] = node.xpath('./div/p/text()')[0].extract()

            yield item
 