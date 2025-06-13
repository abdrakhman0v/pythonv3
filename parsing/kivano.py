from bs4 import BeautifulSoup as bs
import requests
import json
import time

while True:

    URL = 'https://www.kivano.kg/mobilnye-telefony'

    response = requests.get(URL)
    html = response.text
    soup = bs(html, 'lxml')

    phones = soup.find_all('div', class_='item product_listbox oh')

    products = []
    for phone in phones:
        title = phone.find('div', class_='listbox_title oh').text.replace('\n', '')
        price = phone.find('div', class_='listbox_price text-center').text.replace('\n', '').strip()
        img = 'www.kivano.kg' + phone.find('div', class_='listbox_img pull-left').find('img').get('src')
    
        products.append({
            'title':title,
            'price':price,
            'image':img
        })

    with open('kivano_phones.json', 'w') as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

    print("Обновлено! Повторное обновление через час...")
    time.sleep(60 * 60)
