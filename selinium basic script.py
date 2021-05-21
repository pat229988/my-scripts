from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome('D:\chromedriver.exe')

#Opening the site
driver.get("https://atg.party")
print(driver.title)

#Switching to Login page
driver.find_element_by_xpath("/html/body/header/div[1]/div[2]/div/ul/li[2]/a").click()

#Feeding Credentials
email=driver.find_element_by_xpath("//*[@id='email']")
email.send_keys('wiz_saurabh@rediffmail.com')

passw=driver.find_element_by_xpath("//*[@id='password']")
passw.send_keys("Pass@123")

#Pressing Sign IN
driver.find_element_by_xpath("/html/body/header/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/form/div[3]/button").click()
time.sleep(30)

#Switching to Article Page 
#driver.find_element_by_xpath("/html/body/div[2]/div[1]/nav/div/table/tbody/tr/td[1]/div/div/div/a[1]").click()
driver.get("https://atg.party/article")
#time.sleep(10)

#selecting and Feeding Title
title=driver.find_element_by_xpath("//*[@id='title']")
title.send_keys("Fun")

# Selecting and Feeding Description
desc=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[3]/div/form/div[2]/div[1]/div[2]/div").click()

desc1=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[3]/div/form/div[2]/div[1]/div[2]/div")
desc1.send_keys("This is a trial test")

#Uploading Image
driver.find_element_by_xpath("//*[@id='article_pic']").send_keys("/home/user/Downloads/index.jpeg")

#Publishing
driver.find_elemnet_by_xpath("//*[@id='featurebutton']").click()
