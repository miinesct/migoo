#coding=utf-8
import requests
from bs4 import BeautifulSoup as bs

Status = '1'

#看多"走勢數量(十全戰法+ 六脈神劍)=  1   
#看空"走勢數量(十全戰法+ 六脈神劍)=  2

#技術面(爆量長紅+ 成交量排行)= 3
#技術面(多頭吞噬+連3d上漲+ 連3d紅K+漲幅排行)= 4
#技術面(MACD弱轉強(金叉)+ MACD強轉弱(死叉))= 5

#籌碼面(融資連3d增+ 資減+ 融卷連3d增+ 卷減)= 6
#融資增加+融券減少>>散戶看多
#籌碼面(外資4+ 投信2+ 自營2+ 三大法2+ 外資2+ 投信2 +自營2)= 7
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

for case in switch(Status):
    if case('1'): #看多"走勢數量(十全戰法+ 六脈神劍)=  1   
        res = requests.get(r'http://stockwinner.sohowgood.com/TenChart.aspx')
        res1 = requests.get(r'http://stockwinner.sohowgood.com/SixContext.aspx')
        soup = bs(res.text,"html.parser")
        soup1 = bs(res1.text,"html.parser")
        my_string = "/TwStock/Stock.aspx?sno="
        for lind in soup.find_all('a'):
            if  my_string in lind['href']:
                s =  lind['href']
                if len(s.strip(my_string)) == 4:
                    print (s.strip(my_string))
        for lind1 in soup1.find_all('a'):
            if  my_string in lind1['href']:
                s =  lind1['href']
                if len(s.strip(my_string)) == 4:
                    print (s.strip(my_string))
        break
    if case('2'): #看空"走勢數量(十全戰法+ 六脈神劍)=  2
        res = requests.get(r'http://stockwinner.sohowgood.com/TenChart2.aspx')
        res1 = requests.get(r'http://stockwinner.sohowgood.com/SixContext2.aspx')
        soup = bs(res.text,"html.parser")
        soup1 = bs(res1.text,"html.parser")
        my_string = "/TwStock/Stock.aspx?sno="
        for lind in soup.find_all('a'):
            if  my_string in lind['href']:
                s =  lind['href']
                if len(s.strip(my_string)) == 4:
                    print (s.strip(my_string))
        for lind1 in soup1.find_all('a'):
            if  my_string in lind1['href']:
                s =  lind1['href']
                if len(s.strip(my_string)) == 4:
                    print (s.strip(my_string))
        break
    if case('3'): #技術面(爆量長紅+ 成交量排行)= 3
        res = requests.get(r'http://www.sohowgood.com/TwStock/Volume.aspx')
        soup = bs(res.text,"html.parser")
        my_string = "/TwStock/Stock.aspx?stockno="
        for lind in soup.find_all('a'):
            if  my_string in lind['href']:
                s =  lind['href']
                if len(s.strip(my_string)) == 4:
                    print (s.strip(my_string))
        break
    if case('4'):
        res = requests.get(r'http://www.sohowgood.com/TwStock/RankUp.aspx')
        soup = bs(res.text,"html.parser")
        my_string = "/TwStock/Stock.aspx?stockno="
        for lind in soup.find_all('a'):
            if  my_string in lind['href']:
                s =  lind['href']
                if len(s.strip(my_string)) == 4:
                    print (s.strip(my_string))
        break
    if case('5'): #技術面(MACD弱轉強(金叉)+ MACD強轉弱(死叉))= 5
        res = requests.get(r'http://www.sohowgood.com/TwStock/MACD.aspx')
        soup = bs(res.text,"html.parser")
        my_string = "/TwStock/Stock.aspx?stockno="
        for lind in soup.find_all('a'):
            if  my_string in lind['href']:
                s =  lind['href']
                if len(s.strip(my_string)) == 4:
                    print (s.strip(my_string))
        break
    if case('6'): #籌碼面(融資連3d增+ 資減+ 融卷連3d增+ 卷減)= 6
        res = requests.get(r'http://www.sohowgood.com/TwStock/Margin.aspx')
        soup = bs(res.text,"html.parser")
        my_string = "/TwStock/Stock.aspx?stockno="
        for lind in soup.find_all('a'):
            if  my_string in lind['href']:
                s =  lind['href']
                if len(s.strip(my_string)) == 4:
                    print (s.strip(my_string))
        break            
    if case('7'): #籌碼面(外資4+ 投信2+ 自營2+ 三大法2+ 外資2+ 投信2 +自營2)= 7
        res = requests.get(r'http://www.sohowgood.com/TwStock/ThreeLegal.aspx')
        soup = bs(res.text,"html.parser")
        my_string = "/TwStock/Stock.aspx?stockno="
        for lind in soup.find_all('a'):
            if  my_string in lind['href']:
                s =  lind['href']
                if len(s.strip(my_string)) == 4:
                    print (s.strip(my_string))
        break

