from selenium import webdriver
import time
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

class Douyu(object):

    def __init__(self):
        self.url = 'https://www.douyu.com/directory/all'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # opt = webdriver.ChromeOptions()
        # opt.add_argument('--headless')
        # opt.add_argument('--disable-gpu')
        # #opt.add_argument('--window-size=1960,1080')

        # self.driver = webdriver.Chrome(chrome_options=opt)
        # self.driver.maximize_window()
        #self.driver.implicitly_wait(10)
        # WebDriverWait(self.driver,20,0.5).until(EC.presence_of_all_elements_located((By.LINK_TEXT,'下一页')))

    
    def parse_data(self):

        room_list = self.driver.find_elements_by_xpath('//*[@id="listAll"]/section[2]/div[2]/ul/li/div')
        print('begin')
        #print(len(room_list))

        data_list=[]
        for room in room_list :
            temp = {}
            temp['title'] = room.find_element_by_xpath('./a[1]/div[2]/div[1]/h3').text
            temp['type'] = room.find_element_by_xpath('./a[1]/div[2]/div[1]/span').text
            temp['owner'] = room.find_element_by_xpath('./a[1]/div[2]/div[2]/h2').text
            temp['num'] = room.find_element_by_xpath('./a[1]/div[2]/div[2]/span').text
            temp['picture'] = room.find_element_by_xpath('./a[1]/div[1]/div[1]/img').get_attribute('src')
            data_list.append(temp)
        return data_list

    def print_data(self, data_list):
        for data in data_list:
            print(data)            

    def run(self):
        #run
        #driver
        #get
        self.driver.get(self.url)
        #self.driver.find_element_by_xpath('/html/body/div[2]/form/div[1]/button').click()
        time.sleep(1)
        while True:
            time.sleep(5)
            #parse
            data_list = self.parse_data()
            print(len(data_list))
            #print
            self.print_data(data_list)
            #next
            try:
                #el_next = self.driver.find_element_by_xpath('//*[@id="listAll"]/section[2]/div[2]/div/ul/li[9]')
                el_next = self.driver.find_element_by_xpath('//*[contains(text(),"下一页")]')
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                el_next.click()
            except:
                break

    
if __name__ == "__main__":
    douyu = Douyu()
    douyu.run()