import requests
import json
import sys
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
  sys.exit()

url = 'https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2'
request = requests.get(url)
html = BeautifulSoup(request.text, 'html.parser')
text = html.find(id="registerData").string
register_data = json.loads(text)
data = register_data['data']
parsed_data = register_data['parsedData']

if str(sys.argv[1]) == 'summary':
  for item in json.loads(parsed_data):
    if item['Województwo'] == 'Cała Polska':
      infected = int(item['Liczba'])
      dead =  0 if not item['Liczba zgonów'] else int(item['Liczba zgonów'])
      break

  print('infected: {}, dead: {} '.format(infected, dead))

if str(sys.argv[1]) == 'regions':
  print(data)
