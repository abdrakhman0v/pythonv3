from bs4 import BeautifulSoup as bs
import requests
import json

URL = 'https://www.kivano.kg/noutbuki?page='

products = []

def parse_page(url, count):
    respons = requests.get(url + str(count))
    html = respons.text
    soup = bs(html, 'lxml')
    laptops = soup.find_all('div', class_='item product_listbox oh')

    for laptop in laptops:
     
        title = laptop.find('div', class_='listbox_title oh').text 
        img = 'www.kivano.kg' + laptop.find('div', class_='listbox_img pull-left').find('img').get('src')
        price = laptop.find('div', class_='listbox_price text-center').text

        products.append({'title':title.replace('\n', ''),
                       'image':img,
                       'price':price.replace('\n', '')})
     
count = 1
while count !=20:
    parse_page(URL, count)
    print(count)
    count += 1

with open('products.json', 'w') as f:
    json.dump(products, f, ensure_ascii=False, indent=4)

