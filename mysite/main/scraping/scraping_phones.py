import re
import requests
from _decimal import Decimal
from bs4 import BeautifulSoup
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from main.models import Product, ProductCategory
from scraping_errors import *


def scraping():
    url_scraping = 'https://www.niceprice62.ru/telefony/mobilnye-telefony/'
    try:
        resp = requests.get(url_scraping, timeout=10.0)
    except requests.exceptions.Timeout:
        raise ScrapingTimeoutError("request timed out")
    except Exception as e:
        raise ScrapingOtherError(f'{e}')

    if resp.status_code != 200:
        raise ScrapingHTTPError(f"HTTP {resp.status_code}: {resp.text}")

    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')
    blocks = soup.select('.list-tr')
    data_list = []
    for block in blocks:
        data = {}
        name = block.select_one('.list-td-name').get_text().strip()
        data['name'] = name

        image_url = block.select_one('a')
        data['image_url'] = 'https://www.niceprice62.ru/' + re.search(r'data-src=".+"\s{1}',
                                      str(image_url)).group().strip('data-src="').replace('"', '').split()[0]

        data['image_url'] = re.sub('jpe?g', 'webp', data['image_url'])

        if block.select_one('.new-price'):
            price_raw = block.select_one('.new-price').text
            price_raw = Decimal(''.join(re.findall(r'\d+', price_raw)))
            data['price'] = price_raw

        data_list.append(data)

    for dictionary in data_list:
        # имя
        dict_name = dictionary['name']
        name_laptop_full = re.match(r'Смартфон.+', dict_name).group()
        l_name = re.search(r'([a-zA-Z0-9-_",()/]+\s){4}', name_laptop_full).group()

        # name
        descript = dictionary['name'].replace(name_laptop_full, '')
        l_description = ''
        for i in descript:
            if i and i != '\n':
                l_description += i
            if i == '\n':
                l_description += ' '
            l_description = l_description.lstrip()

        if not Product.objects.filter(name=l_name).exists():
            Product.objects.create(
                name=l_name,
                description=l_description,
                price=dictionary['price'],
                image_url=dictionary['image_url'],
                category=ProductCategory(id=2),
            )

if __name__ == '__main__':
    scraping()