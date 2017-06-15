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

解壓縮的exe放置在系統環境變數下

運行Wantgoo.py後，在stock.txt會自動新增符合的股票號碼

再運行OpenWantGoo.py會自動開啟stock.txt內的股票號碼並在Firefox瀏覽器自動貼上玩股網"技術分析-十全戰法"網址

會自動排除成交量低於500張的股票號碼，這時再依據個人經驗挑出股票。

以上教學僅供教育使用
