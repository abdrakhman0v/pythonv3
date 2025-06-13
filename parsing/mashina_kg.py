from bs4 import BeautifulSoup as bs
import requests
import json

URL = 'https://www.mashina.kg/search/all/'

products = []
ID = 1

response = requests.get(URL)
html = response.text
soup = bs(html, 'lxml')

cars = soup.find_all('div', class_='list-item list-label')

for car in cars:
    title = car.find('div', class_='block title').text.strip()
    price = car.find('div', class_='block price').text.strip().replace(' ', '').replace('\n', '.')
    image = car.find('img').get('src')
    year_miles = car.find('p', class_='year-miles').text.strip()
    body_type = car.find('p', class_='body-type').text.strip()
    volume = car.find('p', class_='volume').text.strip()
    
    products.append({
        'id':ID,
        'title':title,
        'price':price,
        'image':image,
        'info':{
            'year-miles':year_miles,
            'body-type':body_type,
            'volume':volume,
        }
    })

    ID += 1

with open('cars_shop.json', 'w') as f:
    json.dump(products, f, ensure_ascii=False, indent=4)