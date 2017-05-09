
#coding=utf-8
from selenium import webdriver #匯入瀏覽器模組
from selenium.webdriver.common.keys import Keys #取得輸入模組
import time
from time import sleep
from selenium.webdriver.chrome.options import Options

def test_1041_CCAA_WIQExcal_download():
    global web
    chrome_options = Options()
    dc = chrome_options.to_capabilities()
    web = webdriver.Remote(
    command_executor = 'http://192.168.21.36:4444/wd/hub', desired_capabilities= dc)
    web.implicitly_wait(10)
    web.get('https://lms.ncu.edu.tw/q?pg=admin_academic_alert_zone&tg=CCAA-searchZone&cx=22.2000&reportType=2')
    Login()
    termBase = web.find_element_by_xpath('//*[@id="termBase"]/option[23]')
    termBase.click()
    division = web.find_element_by_xpath('//*[@id="division"]/option[5]')
    division.click()
    Sbutton = web.find_element_by_xpath('//*[@id="searchAAInfoform"]/div/div[6]/input[3]')
    Sbutton.click()
    try:
        Excelbutton = web.find_element_by_xpath('//*[@id="a_excel"]')
        Excelbutton.click()
        WIQbutton = web.find_element_by_xpath('//*[@id="downloadWord"]')
        WIQbutton.click()
        assert True
    except:
        assert False
    finally:
        web.close()

    
def Login():
    userName=u"ncuadmin1"
    password=u"23yahi12"
    user=web.find_element_by_xpath('//*[@id="login2"]')
    while user.get_attribute('value') !=userName:
        user.clear()
        user.send_keys(userName)
    Pass=web.find_element_by_xpath('//*[@id="password2"]')
    while Pass.get_attribute('value') !=password:
        Pass.clear()
        Pass.send_keys(password)
    loginBtn=web.find_element_by_xpath('//*[@id="trLogin"]/td[2]/input')
    loginBtn.click()

