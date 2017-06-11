'''

此為全自動 單一使用者 從校務系統登入後，申請一SSO帳號

'''
#coding=utf-8
from selenium import webdriver #匯入瀏覽器模組
from selenium.webdriver.common.keys import Keys #取得輸入模組
import time
from time import sleep
import pytesseract #python 控制 tesseract-OCR的模組
from PIL import Image #Pillow = Python image libary 圖片模組
from selenium.webdriver.common.by import By#例外處理模組
from selenium.webdriver.support.ui import WebDriverWait #例外處理模組
from selenium.webdriver.support import expected_conditions as EC #例外處理模組
from selenium.webdriver.common.action_chains import ActionChains #例外處理模組

Status = 'P'
Account = 'P10153076'
Password = '1111'
EmailAC = 'pmac31010@yopmail.com'
Identification = 'U297312920'
SSO_Password = 'gp6nj4'

class switch(object):  #Switch處理
    def __init__(self, value):
        self.value = value
        self.fall = False
 
    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
     
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

def validatePic(): #處理驗證碼
          cc = driver.find_element_by_xpath('//*[@id="validatePic"]')
          if cc.is_displayed() : #判斷驗證碼是否可見
                    driver.implicitly_wait(10)
                    driver.save_screenshot(r'D:/aa.png') #截取當前網頁，為了驗證碼
                    imgelement = driver.find_element_by_xpath('//*[@id="validatePic"]') #定位驗證碼
                    location = imgelement.location #獲取驗證碼XY座標
                    size = imgelement.size #取得驗證碼長寬
                    rangle = (int(location['x'])+1,int(location['y'])+1,int(location['x']+size['width'])-1,int(location['y']+size['height'])-1) #写成我们需要截取的位置坐标
                    #rangle = (X,Y左上角的點,X+物長,Y+物寬右下角的點)
                    i = Image.open(r'D:/aa.png') #打開截圖
                    driver.implicitly_wait(10)
                    frame4=i.crop(rangle) #使用Image的crop函数，從截圖中擷取需要的地方
                    frame4.save(r'D:/12.png')
                    driver.implicitly_wait(10)
                    qq = Image.open(r'D:/12.png').convert('L') #轉換灰階圖 方便OCR處理
                    driver.implicitly_wait(10)
                    Code = pytesseract.image_to_string(qq).strip().replace(' ','') #識別驗證碼to字串.減前後空白.減中間空白
                    return(Code)

driver = webdriver.Firefox()
driver.get('http://210.71.197.145/ecampus_test/Login.action?schNo=100005') #教育局測試高中SSO1
#driver.maximize_window() #螢幕最大化
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="loginId"]').send_keys(Account)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(Password)
Code = validatePic() #呼叫驗證碼程式
driver.find_element_by_xpath('//*[@id="validateCode"]').send_keys(Code)
driver.find_element_by_xpath('//*[@id="login"]').click()
try: #例外處理(如果輸驗證碼輸入錯誤，會跳出視窗)
    while WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]'))) != None :
        driver.find_element_by_xpath('/html/body/div[3]/div[11]/button/span').click()
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(Password)
        Code = validatePic()
        if len(Code) != 4 :
                  Code = 'null'
        driver.find_element_by_xpath('//*[@id="validateCode"]').send_keys(Code)
        driver.find_element_by_xpath('//*[@id="login"]').click()
finally: #輸入驗證碼正確後，會執行以下
    for case in switch(Status):
          if case('T'):
                    driver.find_element_by_xpath('//*[@id="BottomFunctionBar"]/button[3]').click() #申請帳號
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath('/html/body/div[9]/div[11]/button[2]/span').click()
                    sleep(5)
                    driver.find_element_by_xpath('//*[@id="dataBean.teacher.account"]').send_keys(EmailAC)
                    if driver.find_element_by_xpath('//*[@id="dataBean.teacher.account"]') != EmailAC :
                              driver.find_element_by_xpath('//*[@id="dataBean.teacher.account"]').clear()
                              driver.find_element_by_xpath('//*[@id="dataBean.teacher.account"]').send_keys(EmailAC)
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath('//*[@id="dataBean.teacher.telephone"]').clear() #電話
                    driver.find_element_by_xpath('//*[@id="dataBean.teacher.idcard"]').clear()  #身分證
                    driver.find_element_by_xpath('//*[@id="dataBean.teacher.idcard"]').send_keys(Identification)
                    driver.find_element_by_xpath('//*[@id="dataBean.teacher.password"]').send_keys(SSO_Password)
                    driver.find_element_by_xpath('//*[@id="repeatPassword"]').send_keys(SSO_Password)
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath('//*[@id="teacherRegisterForm"]/div[1]/div/div[4]/center/input').click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath('//*[@id="teacherRegisterForm"]/div[1]/div/div[4]/center/input[2]').click()
                    print('已完成校務系統申請SSO帳號')
                    #text = input('按任意鍵離開')
                    driver.close()
                    break
          elif case('S'):
                    driver.find_element_by_xpath('//*[@id="BottomFunctionBar"]/button[3]').click() #申請帳號
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath('/html/body/div[9]/div[11]/button[2]/span').click()
                    sleep(5)
                    driver.find_element_by_xpath('//*[@id="dataBean.student.account"]').send_keys(EmailAC)
                    if driver.find_element_by_xpath('//*[@id="dataBean.student.account"]') != EmailAC :
                              driver.find_element_by_xpath('//*[@id="dataBean.student.account"]').clear()
                              driver.find_element_by_xpath('//*[@id="dataBean.student.account"]').send_keys(EmailAC)
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath('//*[@id="dataBean.student.telephone"]').clear() #電話
                    driver.find_element_by_xpath('//*[@id="dataBean.student.idcard"]').clear()  #身分證
                    driver.find_element_by_xpath('//*[@id="dataBean.student.idcard"]').send_keys(Identification)
                    driver.find_element_by_xpath('//*[@id="dataBean.student.password"]').send_keys(SSO_Password)
                    driver.find_element_by_xpath('//*[@id="repeatPassword"]').send_keys(SSO_Password)
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath('//*[@id="studentRegisterForm"]/div[1]/div/div[4]/center/input').click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath('//*[@id="studentRegisterForm"]/div[1]/div/div[4]/center/input[2]').click()
                    print('已完成校務系統申請SSO帳號')
                    #text = input('按任意鍵離開')
                    driver.close()
                    break
          elif case('P'):
                    driver.find_element_by_xpath('//*[@id="BottomFunctionBar"]/button[3]').click() #申請帳號
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath('/html/body/div[9]/div[11]/button[2]/span').click()
                    sleep(5)
                    driver.find_element_by_xpath('//*[@id="dataBean.parent.account"]').send_keys(EmailAC)
                    if driver.find_element_by_xpath('//*[@id="dataBean.parent.account"]') != EmailAC :
                              driver.find_element_by_xpath('//*[@id="dataBean.parent.account"]').clear()
                              driver.find_element_by_xpath('//*[@id="dataBean.parent.account"]').send_keys(EmailAC)
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath('//*[@id="dataBean.parent.telephone"]').clear() #電話
                    driver.find_element_by_xpath('//*[@id="dataBean.parent.idcard"]').clear()  #身分證
                    driver.find_element_by_xpath('//*[@id="dataBean.parent.idcard"]').send_keys(Identification)
                    driver.find_element_by_xpath('//*[@id="dataBean.parent.password"]').send_keys(SSO_Password)
                    driver.find_element_by_xpath('//*[@id="repeatPassword"]').send_keys(SSO_Password)
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath('//*[@id="parentRegisterForm"]/div[1]/div/div[4]/center/input').click()
                    driver.implicitly_wait(10)
                    driver.find_element_by_xpath('//*[@id="parentRegisterForm"]/div[1]/div/div[4]/center/input[2]').click()
                    print('已完成校務系統申請SSO帳號')
                    #text = input('按任意鍵離開')
                    driver.close()
                    break
                    
