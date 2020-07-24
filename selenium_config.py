from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'https://www.ptt.cc/bbs/Beauty/index.html'

opt = webdriver.ChromeOptions()

opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
opt.add_argument('--window-size=1960,1080')

driver = webdriver.Chrome(chrome_options=opt)
driver.maximize_window()
# driver.fullscreen_window()
driver.get(url)
driver.save_screenshot('表特版.png')
print(driver.get_window_position())
print(driver.get_window_size())
print(driver.get_window_rect())