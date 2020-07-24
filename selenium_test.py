import time
from selenium import webdriver

# driver = webdriver.Chrome(executable_path='D:\皓中\chromedriver.exe')
driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# driver.find_element_by_id('kw').send_keys('python')
# driver.find_element_by_id('su').click()
driver.get("https://www.google.com")
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys('python')
#driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]').click()
driver.find_elements_by_partial_link_text('Google 搜尋').click()
time.sleep(6)
driver.quit()