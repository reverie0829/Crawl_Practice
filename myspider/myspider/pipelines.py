# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class MyspiderPipeline:

    def __init__(self):
        self.file = open('itcast.json', 'w')
        
    
    def process_item(self, item, spider):
        #print('itcast : ',item)
        #將item對象 強轉字典 該操作只能在scrapy中使用
        item = dict(item)

        #將字典數據序列化
        json_data = json.dumps(item) + ',\n'
        #json_data = json.dumps(item , ensure_ascii=False) + ',\n'  //中文保存

        #將數據寫入文件
        self.file.write(json_data)

        #默認使用玩pipeline後要將數據返回給引擎
        return item


    def __del__(self):
        self.file.close()