#-*- coding:utf-8 -*-
#Use Python2.7 By Micheng
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

address=u'.\\stock.txt'   #股票txt檔案位置
fp=open(address,'r')
number=[]
lines=fp.readlines()
for data in lines:
    number.extend(data.strip().split(','))  #刪除空白並以,分割成陣列['3231','1234']
fp.close()

web = webdriver.Firefox()
handles=lambda:web.window_handles
for i in range(len(number)):
    url= 'http://www.wantgoo.com/stock/astock/techchart?StockNo=%s&m=ten' %number[i]
    web.get(url)
    vol = web.find_element_by_xpath('//*[@id="container"]/div[3]/div[2]/ul/li[5]/b').text   #取得成交張數
    vol1=vol.replace(',','')    #移除字串的,
    array=handles()
    arrayNum=len(array) #取得現有的總Tab數量
    if arrayNum!=1:
        if vol1=='--' or int(vol1)<500:  #小於500張即關閉該Tab
            web.close()
            array=handles()
            arrayNum=len(array)
            web.switch_to_window(web.window_handles[arrayNum-1]) #切換回上一個Tab
    if i%30==0 and i!=0:    #開啟30個分頁後，等待使用者輸入Enter才繼續，避免Firefox吃光記憶體
        raw_input('Now i= '+str(i)+' ,Total '+str(len(number)))
        array=handles()
        arrayNum=len(array)
        web.switch_to_window(web.window_handles[arrayNum-1]) #切換回上一個Tab
    web.find_element_by_tag_name('body').send_keys(Keys.CONTROL  + 't') #新增一空白Tab
    array=handles()
    arrayNum=len(array) #取得現有的總Tab數量
    web.switch_to_window(web.window_handles[arrayNum-1])
