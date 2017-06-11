'''
For WiNCU 專案，下拉式選單自動化組合搜索，並截圖比對資料的正確性
'''
#coding=utf-8
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time
#import util
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.select import Select


UserAC = 'superadmin'   #自行更改
AC_Password = '123456q'    

driver = webdriver.Firefox()
          #WiNCU web link
url = 'https://lms.ncu.edu.tw/q?pg=classes_all&tg=Academics-list&cmp=R22.0_108&cx=22.2000'
driver.get(url)
driver.maximize_window() #螢幕最大化
sleep(2)
driver.implicitly_wait(10)
spy = 0
sel0 = lambda: driver.find_element_by_xpath('//*[@id="termBase"]')
sel00  = sel0().find_elements_by_tag_name('option')
tsel0 = len(sel00)
sel1 = lambda: driver.find_element_by_xpath('//*[@id="dept"]')
sel11  = sel1().find_elements_by_tag_name('option')
tsel1 = len(sel11)
search = lambda: driver.find_element_by_xpath('//*[@id="search_button"]')
width  = lambda: driver.execute_script("return Math.max(document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth);")
height = lambda: driver.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")

#s1 = Select(driver.find_element_by_xpath('s1Id'))
#s1.select_by_index(1)
for x in range(tsel0):
          linkssss = sel0().find_elements_by_tag_name('option')
          linkkkk = linkssss[x]
          linkkkk.click()
          for y in range(tsel1):
                    linksss = sel1().find_elements_by_tag_name('option')
                    linkkk = linksss[y]
                    linkkk.click()
                    search().click()
                    sleep(2)
                    driver.maximize_window()
                    driver.set_window_size(width()+100, height()+100)
                    sleep(2)
                    driver.save_screenshot(r'D:/testPic/%s.png' %spy)
                    spy+=1
                    
'''
driver.find_element_by_xpath('//*[@id="loginId"]').send_keys(UserAC)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(AC_Password)
Code = validatePic() #呼叫驗證碼程式
driver.find_element_by_xpath('//*[@id="verifyCode"]').send_keys(Code)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/div[1]/div[2]/table/tbody/tr[4]/td[2]/input[1]').click()
try: #例外處理(如果輸驗證碼輸入錯誤，會跳出視窗)
    while WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button'))) != None :
        driver.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button').click()
        if driver.find_element_by_xpath('//*[@id="loginId"]').text != UserAC:
                  driver.find_element_by_xpath('//*[@id="loginId"]').clear()
                  driver.find_element_by_xpath('//*[@id="loginId"]').send_keys(UserAC)
        driver.find_element_by_xpath('//*[@id="password"]').clear()
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(AC_Password)
        driver.find_element_by_xpath('//*[@id="verifyCode"]').clear()
        driver.find_element_by_xpath('//*[@id="virifyCode"]').click()
        sleep(1)
        Code = validatePic()
        if len(Code) != 4:
                  Code = 'Null'
        driver.find_element_by_xpath('//*[@id="verifyCode"]').send_keys(Code)
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/div[1]/div[2]/table/tbody/tr[4]/td[2]/input[1]').click()
finally: #輸入驗證碼正確後，會執行以下
          
          #driver.find_element_by_xpath('//*[@id="school"]/li[2]/a').click()
          driver.find_element_by_xpath('//*[@id="teacher_manage"]').click()
          for i in range(10):
                    path = '//*[@id="userInfoList"]/tbody/tr[1]/th[%s]/img' % (i+2)
                    driver.find_element_by_xpath(path).click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath(path).click()
          driver.find_element_by_xpath('//*[@id="logo1"]').click()

   #學生管理       
          driver.find_element_by_xpath('//*[@id="stu_manage"]').click()
          sel0 = lambda: driver.find_element_by_xpath('//*[@id="condition.schoolYear"]')
          sel00  = sel0().find_elements_by_tag_name('option')
          tsel0 = len(sel00)
          sel1 = lambda: driver.find_element_by_xpath('//*[@id="condition.termId"]')
          sel11  = sel1().find_elements_by_tag_name('option')
          tsel1 = len(sel11)
          sel2 = lambda: driver.find_element_by_xpath('//*[@id="condition.gradeId"]')
          sel22  = sel2().find_elements_by_tag_name('option')
          tsel2 = len(sel22)
          sel3 = lambda: driver.find_element_by_xpath('//*[@id="condition.groupId"]')
          sel33  = sel3().find_elements_by_tag_name('option')
          tsel3 = len(sel33)
          search = lambda: driver.find_element_by_xpath('//*[@id="accountForm"]/div/div[2]/div[1]/div/input[2]')
          
          for x in range(tsel0):
                    linkssss = sel0().find_elements_by_tag_name('option')
                    linkkkk = linkssss[x]
                    linkkkk.click()
                    for y in range(tsel1):
                              linksss = sel1().find_elements_by_tag_name('option')
                              linkkk = linksss[y]
                              linkkk.click()
                              for z in range(tsel2):
                                        linkss = sel2().find_elements_by_tag_name('option')
                                        linkk = linkss[z]
                                        linkk.click()
                                        sel33  = sel3().find_elements_by_tag_name('option')
                                        tsel3 = len(sel33)
                                        for z1 in range(tsel3):
                                                  links = sel3().find_elements_by_tag_name('option')
                                                  link = links[z1]
                                                  link.click()
                                                  search().click()
          driver.find_element_by_xpath('//*[@id="logo1"]').click()

#Cloud 學校設定
          driver.switch_to.frame('iframe')
          driver.switch_to.frame(driver.find_element_by_css_selector('#leftSideTop'))
          driver.find_element_by_xpath('//*[@id="leftSide"]/div/button[1]').click()
          driver.switch_to.default_content()
          driver.switch_to.frame('iframe')
          driver.switch_to.frame(driver.find_element_by_css_selector('#leftSide'))
          driver.find_element_by_xpath('//*[@id="cloud_021"]').click()
          driver.switch_to.default_content()
          driver.switch_to.frame('iframe')
          driver.switch_to.frame(driver.find_element_by_css_selector('#mainFrame'))
          driver.switch_to.frame(driver.find_element_by_css_selector('#iFramecloud_021'))
          sel0 = lambda: driver.find_element_by_xpath('//*[@id="search"]/div/table/tbody/tr[1]/td[6]/select')
          sel00  = sel0().find_elements_by_tag_name('option')
          tsel0 = len(sel00)
          sel1 = lambda: driver.find_element_by_xpath('//*[@id="schoolInfo.provinceCode"]')
          sel11  = sel1().find_elements_by_tag_name('option')
          tsel1 = len(sel11)
          sel2 = lambda: driver.find_element_by_xpath('//*[@id="schoolInfo.cityCode"]')
          sel22  = sel2().find_elements_by_tag_name('option')
          tsel2 = len(sel22)
          sel3 = lambda: driver.find_element_by_xpath('//*[@id="schoolInfo.areaCode"]')
          sel33  = sel3().find_elements_by_tag_name('option')
          tsel3 = len(sel33)
          search = lambda: driver.find_element_by_xpath('//*[@id="search"]/div/table/tbody/tr[3]/td[6]/input[1]')
          
          for x in range(tsel0):
                    linkssss = sel0().find_elements_by_tag_name('option')
                    linkkkk = linkssss[x]
                    linkkkk.click()
                    driver.implicitly_wait(10)
                    for y in range(tsel1):
                              linksss = sel1().find_elements_by_tag_name('option')
                              linkkk = linksss[y]
                              linkkk.click()
                              sel22  = sel2().find_elements_by_tag_name('option')
                              tsel2 = len(sel22)
                              for z in range(tsel2):
                                        try: #例外處理(如果輸驗證碼輸入錯誤，會跳出視窗)
                                                            while WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="schoolInfo.cityCode"]'))) == None :
                                                                      linkss = sel2().find_elements_by_tag_name('option')
                                                                      linkk = linkss[z]
                                                                      linkk.click()
                                        except NoSuchElementException:
                                                  time.sleep(1)
                                        sel33  = sel3().find_elements_by_tag_name('option')
                                        tsel3 = len(sel33)
                                        for z1 in range(tsel3):
                                                  try: #例外處理(如果輸驗證碼輸入錯誤，會跳出視窗)
                                                            while WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="schoolInfo.areaCode"]'))) != None :
                                                                      links = sel3().find_elements_by_tag_name('option')
                                                                      link = links[z1]
                                                                      link.click()
                                                                      search().click()
                                                  except NoSuchElementException:
                                                            time.sleep(1)
                                                
'''
          

