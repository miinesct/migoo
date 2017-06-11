# migoo
使用Python 2.7

# 半自動化找出當日翻多的股票

使用玩股網wantgoo的十全戰法進行判斷
過濾出今日"偏多"的股票

程式相依套件
pip install -U selenium
pip install requests
pip install BeautifulSoup4

下載Firefox最新版本+geckodriver
https://github.com/mozilla/geckodriver/releases
解壓縮的exe放置在環境變數下

使用Wantgoo.py列印出當日翻多的股票，將結果複製貼上到stock.txt內

再使用OpenWantGoo.py來開啟stock.txt內的股票號碼

會自動排除成交量低於500張的股票號碼，再依據經驗挑出股票
