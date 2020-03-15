import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2'
request = requests.get(url)
html = BeautifulSoup(request.text, 'html.parser')
text = html.find(id="registerData").string
json = json.loads(text)
data = json['data']
print(data)
