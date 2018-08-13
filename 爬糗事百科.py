# coding=utf-8
import re
import requests

str_url = 'https://www.qiushibaike.com/8hr/page/{}/'
# 模拟浏览器
for i in range(13):
    url =   str_url.format(i + 1)
    headers = {'''
    User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36
    '''}

    reseponse = requests.get(url)
    result = reseponse.content.decode()


    ret_list = re.findall(r'<div class="content">.*?<span>(.*?)</span>.*?</div>',result,re.S)       #re.S  能够匹配到换行符
    with open('糗事百科.txt','a',encoding='utf8') as f:
        for i in ret_list:
            res = re.sub('<br/>|\\n','',i)     #  把<br/> 替换成 空（'原来的' ,'替换后的东西'，i）
            f.write(res+'\n\n')


