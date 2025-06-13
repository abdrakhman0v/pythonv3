from bs4 import BeautifulSoup as bs
import requests
import json

URL = 'https://www.mashina.kg/'

products = []

response = requests.get(URL)
html = response.text
soup = bs(html, 'lxml')

blocks_car = soup.find_all('div', class_='category-block cars')

for block in blocks_car:
    cars = block.find_all('div', class_='category-block-content-item')
    for car in cars:
        title = car.find('div', class_='main-title').text.strip().replace('\n', '')
        price = car.find('p', class_='price').text.strip().replace('\n', '| ')
        
        products.append({
            'category':'Легковой авто',
            'title':title,
            'price':price
        })
        
blocks_commercial = soup.find_all('div', class_='category-block commercial')

for block in blocks_commercial:
    commercials = block.find_all('div', class_='c')
    for com in commercials:
        title = com.find('div', class_='main-title').text.strip().replace('\n', '').replace(" ","")
        price = com.find('p', class_='price').text.strip().replace(' ', '').replace('\n', '| ')

        products.append({
            'category':'Коммерчиский авто',
            'title':title,
            'price':price
        })

blocks_spec = soup.find_all('div', class_='category-block spec')

for block in blocks_spec:
    specs = block.find_all('div', class_='category-block-content-item')
    for spec in specs:
        title = spec.find('div', class_='main-title').text.strip().replace('\n', '').replace(" ","")
        price = spec.find('p', class_='price').text.strip().replace(' ', '').replace('\n', '| ')
        
        products.append({
            'category':'Спецтехника',
            'title':title,
            'price':price
        })

blocks_parts = soup.find_all('div', class_='category-block parts')

for block in blocks_parts:
    parts = block.find_all('div', class_='category-block-content-item')
    for part in parts:
        title = part.find('div', class_='main-title').text.strip().replace('\n', '')
        price = part.find('p', class_='price').text.strip().replace(' ', '').replace('\n', '| ')

        products.append({
            'category':'Запчасть',
            'title':title,
            'price':price
        })

blocks_service = soup.find_all('div', class_='category-block service')

for block in blocks_service:
    services = block.find_all('div', class_='category-block-content-item')
    for service in services:
        title = service.find('div', class_='main-title').text.strip().replace('\n', '')
        price = service.find('p', class_='price').text.strip().replace(' ', '').replace('\n', '| ')

        products.append({
            'category':'Услуга',
            'title':title,
            'price':price
        })

blocks_moto = soup.find_all('div', class_='category-block moto')

for block in blocks_moto:
    motos = block.find_all('div', class_='category-block-content-item')
    for moto in motos:
        title = moto.find('div', class_='main-title').text.strip().replace('\n', '').replace(' ', '')
        price = moto.find('p', class_='price').text.strip().replace(' ', '').replace('\n', '| ')
        
        products.append({
            'category':'Мото',
            'title':title,
            'price':price
        })

blocks_buy = soup.find_all('div', class_='category-block buy')

for block in blocks_buy:
    buys = block.find_all('div', class_='category-block-content-item')
    for buy in buys:
        title = buy.find('div', class_='main-title').text.strip().replace('\n', '')
        price = buy.find('p', class_='price').text.strip().replace(' ', '').replace('\n', '| ')
        
        products.append({
            'category':'Куплю',
            'title':title,
            'price':price
        })

with open('cars_shop.json', 'w') as f:
    json.dump(products, f, ensure_ascii=False, indent=4)
    