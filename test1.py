#coding=utf-8
from selenium import webdriver #匯入瀏覽器模組
from selenium.webdriver.common.keys import Keys #取得輸入模組
import time
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains as AC
import os

def paste_keys(xpath, text):
    os.system("echo %s| clip" % text.strip())
    el = driver.find_element_by_xpath(xpath)
    el.send_keys(Keys.CONTROL, 'v')

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://stage.tibame.net/login')
#driver.maximize_window() #螢幕最大化
paste_keys('//*[@id="content"]/div/div[3]/div/div[2]/form/div/div[3]/input',u"jj40@jj.com")
paste_keys('//*[@id="content"]/div/div[3]/div/div[2]/form/div/div[4]/input',u"123456")
loginBtn=driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/div[2]/form/div/div[6]/button')
loginBtn.click()
#進入學習中心
name = driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/div[1]/div[2]/p').text
assert name == 'Mr.J40'
sleep(3)
driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div/button').click()
sleep(2)
driver.execute_script('document.getElementsByTagName("video")[0].pause()')
videotime1 =driver.find_element_by_xpath('//*[@id="vjs_video_3"]/div[5]/div[5]/div/div[3]')
print videotime1.get_attribute('data-current-time')
driver.execute_script('document.getElementsByTagName("video")[0].play()')
sleep(2)
driver.execute_script('document.getElementsByTagName("video")[0].pause()')
videotime2 =driver.find_element_by_xpath('//*[@id="vjs_video_3"]/div[5]/div[5]/div/div[3]')
print videotime2.get_attribute('data-current-time')
#影片播放play()，暫停pause()
#data-current-time 時間
driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/div[1]/div[1]/div/img').click()
driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/div[1]/div[1]/a').click()
#完成影片測試返回

menu = driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/div[2]/div/div/div[3]/div/div[2]/div/div')
hidden_submenu = driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div[3]/button')

AC(driver).move_to_element(menu).click(hidden_submenu).perform()

driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/div[1]/div[1]/a').click()
#返回

paste_keys('//*[@id="content"]/div/div[3]/div/div[2]/div/div/div[2]/div[1]/div/div/div/input','Node')
driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/div[2]/div/div/div[2]/div[1]/div/div/button').click()
#我的課程搜尋
driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/div[1]/div[3]/ul/a[2]/li').click()
paste_keys('//*[@id="content"]/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div/div/input','Node')
driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div/button').click()
#我的收藏搜尋











