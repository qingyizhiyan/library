import requests,re
from bs4 import BeautifulSoup
txt = ''
url = input('the url:')
cookies = input('the cookies:')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
           'cookie':cookies if cookies else ''}
try:
    response = requests.get(url,headers=headers,timeout=60)
    soup = BeautifulSoup(response.text, 'html.parser')
    print("FINISHED")
    txt = soup.prettify()
except:
    print("FAILED")
def pa():
    pattern = (r'<a rel="noopener" href="/p/[0-9]+" title="(.+?)" target="_blank" class="j_th_tit ">.+?</a>'
            r'\s*</div><div class="threadlist_author pull_right">'
            r'\s*<span class="tb_icon_author "'
            r'\s*title="主题作者: (.+)"'
            r'\s*data-field=.+?'
            r'\s*<span class="pull-right is_show_create_time" title="创建时间">(\S+?)</span>'
            r'\s*</div>'
            r'\s*</div>'
            r'\s*<div class="threadlist_detail clearfix">'
            r'\s*<div class="threadlist_text pull_left">'
            r'\s*<div class="threadlist_abs threadlist_abs_onlyline ">'
            r'\s*(.+)'
            r'\s*</div>')
    l = re.findall(pattern,txt)
    for i in l:
        print(i[0],"\n","作者: "+i[1],"\n","时间: "+i[2],"\n",i[3],"\n",sep='')
