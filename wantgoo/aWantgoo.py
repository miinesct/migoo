#coding=utf-8
import requests
from bs4 import BeautifulSoup as bs

array1 = []
array2 = []

res = requests.get(r'http://stockwinner.sohowgood.com/TenChart.aspx')
res1 = requests.get(r'http://stockwinner.sohowgood.com/SixContext.aspx')
soup = bs(res.text,"html.parser")
soup1 = bs(res1.text,"html.parser")
href_link = "/TwStock/Stock.aspx?sno="
for lind in soup.find_all('a'):
  if  href_link in lind['href']:
      s =  lind['href']
      if len(s.strip(href_link)) == 4:
          array1.append((s.strip(href_link)))
for lind1 in soup1.find_all('a'):
  if  href_link in lind1['href']:
      s =  lind1['href']
      if len(s.strip(href_link)) == 4:
          array1.append((s.strip(href_link)))
res = requests.get(r'http://www.sohowgood.com/TwStock/Volume.aspx')
soup = bs(res.text,"html.parser")
href_link = "/TwStock/Stock.aspx?stockno="
for lind in soup.find_all('a'):
  if  href_link in lind['href']:
      s =  lind['href']
      if len(s.strip(href_link)) == 4:
          array1.append((s.strip(href_link)))
res = requests.get(r'http://www.sohowgood.com/TwStock/RankUp.aspx')
soup = bs(res.text,"html.parser")
href_link = "/TwStock/Stock.aspx?stockno="
for lind in soup.find_all('a'):
  if  href_link in lind['href']:
      s =  lind['href']
      if len(s.strip(href_link)) == 4:
          array1.append((s.strip(href_link)))
array2 = sorted(set(array1),key=array1.index)
address=u'.\\stock.txt'   #股票txt檔案位置
fp=open(address,'w+')
fp.seek(0)
for i in range(len(array2)):
    fp.write(array2[i]+'\n')
fp.close()
