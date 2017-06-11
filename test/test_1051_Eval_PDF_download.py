
#coding=utf-8
from selenium import webdriver #匯入瀏覽器模組
from selenium.webdriver.common.keys import Keys #取得輸入模組
import time
from time import sleep
from selenium.webdriver.chrome.options import Options

def test_1051_Eval_download():
    global web
    chrome_options = Options()
    dc = chrome_options.to_capabilities()
    web = webdriver.Remote(
    command_executor = 'http://192.168.21.36:4444/wd/hub', desired_capabilities= dc)
    web.implicitly_wait(10)
    web.get('https://lms.ncu.edu.tw/q?pg=reportz_zone&tg=reportz_zoneTg&cmp=R22.0_530&cx=22.2000')
    Login()
    termBase = web.find_element_by_xpath('//*[@id="termBase"]/option[25]')
    termBase.click()
    division = web.find_element_by_xpath('//*[@id="division"]/option[6]')
    division.click()
    department = web.find_element_by_xpath('//*[@id="department"]/option[3]')
    department.click()
    Sbutton = web.find_element_by_xpath('//*[@id="showFacultyList"]/span[2]')
    Sbutton.click()
    try:
        PDFbutton = web.find_element_by_xpath('//*[@id="a_evalpdf"]')
        PDFbutton.click()
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




