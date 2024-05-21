import requests
from bs4 import BeautifulSoup
txt = ''
url = input('the url:')
cookies = input('the cookies:')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763','cookie':cookies if cookies else ''}
try:
    response = requests.get(url,headers=headers,timeout=60)
    soup = BeautifulSoup(response.text, 'html.parser')
    print("FINISHED")
    txt = soup.prettify()
except:
    print("FAILED")
