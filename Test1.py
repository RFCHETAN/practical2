#from selenium import webdriver

#from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome(executable_path="C:\\Users\\Chetan Ramesh\\Desktop\\Selenium2021\\chromedriver.exe")
#driver.get("https://www.google.com")
#print(driver.title)
#driver.maximize_window()
#driver.close()
import time

from selenium import  webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\Chetan Ramesh\\Desktop\\Selenium2021\\chromedriver.exe")
driver.get("https://www.google.com")
driver.maximize_window()
driver.get("https://www.bing.com")
print(driver.current_url)
driver.maximize_window()
time.sleep(2)
driver.back()
