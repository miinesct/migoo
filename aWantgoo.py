#coding=utf-8
import requests
from bs4 import BeautifulSoup as bs

Status = '0'

l1 = []
l2 = []
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
    if case('0'): #看多"走勢數量(十全戰法+ 六脈神劍)=  1   
        res = requests.get(r'http://stockwinner.sohowgood.com/TenChart.aspx')
        res1 = requests.get(r'http://stockwinner.sohowgood.com/SixContext.aspx')
        soup = bs(res.text,"html.parser")
        soup1 = bs(res1.text,"html.parser")
        my_string = "/TwStock/Stock.aspx?sno="
        for lind in soup.find_all('a'):
            if  my_string in lind['href']:
                s =  lind['href']
                if len(s.strip(my_string)) == 4:
                    l1.append((s.strip(my_string)))
        for lind1 in soup1.find_all('a'):
            if  my_string in lind1['href']:
                s =  lind1['href']
                if len(s.strip(my_string)) == 4:
                    l1.append((s.strip(my_string)))
        res = requests.get(r'http://www.sohowgood.com/TwStock/Volume.aspx')
        soup = bs(res.text,"html.parser")
        my_string = "/TwStock/Stock.aspx?stockno="
        for lind in soup.find_all('a'):
            if  my_string in lind['href']:
                s =  lind['href']
                if len(s.strip(my_string)) == 4:
                    l1.append((s.strip(my_string)))
        res = requests.get(r'http://www.sohowgood.com/TwStock/RankUp.aspx')
        soup = bs(res.text,"html.parser")
        my_string = "/TwStock/Stock.aspx?stockno="
        for lind in soup.find_all('a'):
            if  my_string in lind['href']:
                s =  lind['href']
                if len(s.strip(my_string)) == 4:
                    l1.append((s.strip(my_string)))
        break
l2 = sorted(set(l1),key=l1.index)
#l2 = {}.fromkeys(l1).keys()
for i in range(len(l2)):
    print l2[i]
