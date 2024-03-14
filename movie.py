import requests,re
url = 'https://ssr1.scrape.center/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
response = requests.get(url,headers=headers)
pattern1 = r'<h2 data-v-7f856186="" class="m-b-sm">([\u4e00-\u9fff]+) - (.+?(?=</h2>))'
pattern2 = r'\b\d\.\d\b'
#没有单词边界会导致l2元素过多
l1 = re.findall(pattern1,response.text)
l2 = re.findall(pattern2,response.text)
for i in range(len(l2)):
    print(f"{l1[i][0]}，英文名{l1[i][1]}，评分{l2[i]}")
