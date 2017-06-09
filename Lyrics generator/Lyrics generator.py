#coding=utf-8
import requests
from bs4 import BeautifulSoup
import json
import re
import os  
import sys
from random import randint  
import jieba

filename='C:\\Users\\10602305\\Desktop\\Lyrics generator\\lyic.txt'
'''
#分詞遇到error時使用
if sys.getdefaultencoding() != 'utf-8':  
    reload(sys)
    sys.setdefaultencoding('utf-8')
'''
def cut_words(filename):  
    with open(filename) as f:
        content = f.read()
        seg_list = jieba.cut(content, cut_all=False)
        word_list = [str(x) for x in seg_list if x not in ['', ' ']]
        with open('words.txt', 'w') as wf:
            wf.write(' / '.join(word_list))
    return None

def get_word_list(filename):  
    with open(filename) as f:
        content = f.read()
        word_list = content.split(' / ')
        return word_list
    return None

def build_word_dict(word_list):  
    word_dict = {}
    for i in range(0, len(word_list)-2):
        if word_list[i] not in word_dict:
            word_dict[word_list[i]] = {}
        if word_list[i+1] not in word_dict[word_list[i]]:
            word_dict[word_list[i]][word_list[i+1]] = 0
        word_dict[word_list[i]][word_list[i+1]] += 1
    return word_dict

def get_random_word(sub_word_dict):  
    index = randint(0, len(sub_word_dict)-1)
    return sub_word_dict.keys()[index]

if __name__ == "__main__":
    if not os.path.exists('words.txt'):
        cut_words(filename)
    word_list = get_word_list('C:\\Users\\10602305\\Desktop\\Lyrics generator\\words.txt')
    word_dict = build_word_dict(word_list)
    length = 100
    chain = ""
    current = "我"
    for i in range(0, length):
        chain += current
        current = get_random_word(word_dict[current])
    print chain
    
'''
#陳奕迅熱門前50歌詞下載
singer_url = 'http://music.163.com/artist?id=' + str(2116)
print singer_url
web_data = requests.get(singer_url)
soup = BeautifulSoup(web_data.text, 'html.parser')
singer_name = soup.select("#artist-name")
r = soup.find('ul', {'class': 'f-hide'}).find_all('a')
r = (list(r))
music_id_set=[]
for each in r:
    song_name = each.text  # print(each.text)
    song_id = each.attrs["href"]
    music_id_set.append(song_id[9:])

for i in range(len(music_id_set)):
    lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + music_id_set[i] + '&lv=1&kv=1&tv=-1'
    lyric = requests.get(lrc_url)
    json_obj = lyric.text
    j = json.loads(json_obj)
    lrc = j['lrc']['lyric']
    pat = re.compile(r'\[.*\]')
    lrc = re.sub(pat, "", lrc)
    lrc = lrc.strip()
    print lrc
'''
