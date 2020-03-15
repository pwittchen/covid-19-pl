import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2'
request = requests.get(url)
soup = BeautifulSoup(request.text, 'html.parser')
register_data = soup.find(id="registerData").string
register_data_json = json.loads(register_data)
print(register_data_json['data'])
