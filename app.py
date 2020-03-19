import requests
import json
import sys
from bs4 import BeautifulSoup

def get_register():
  url = 'https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2'
  request = requests.get(url)
  html = BeautifulSoup(request.text, 'html.parser')
  text = html.find(id="registerData").string
  return json.loads(text)

def get_region(region):
  register = get_register()
  for item in json.loads(register['parsedData']):
    if item['Województwo'] == region:
      infected = int(item['Liczba'])
      dead =  0 if not item['Liczba zgonów'] else int(item['Liczba zgonów'])
      break
  print('infected;dead')
  print('{};{}'.format(infected, dead))

def main():
  if str(sys.argv[1]) == 'summary':
    get_region('Cała Polska')
  if str(sys.argv[1]) == 'regions':
    print(get_register()['data'])
  if str(sys.argv[1]) == 'region':
    get_region(str(sys.argv[2]))

main()
