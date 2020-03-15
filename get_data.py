import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2'
request = requests.get(url)
html = BeautifulSoup(request.text, 'html.parser')
register = json.loads(html.find(id="registerData").string)
print(register['data'])
