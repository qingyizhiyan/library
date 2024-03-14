import requests,re
url = 'https://ssr1.scrape.center/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
response = requests.get(url,headers=headers)
pattern = r'<h2 data-v-7f856186="" class="m-b-sm">([\u4e00-\u9fff]+) - (.+?(?=</h2>))'
print(re.findall(pattern,response.text))
