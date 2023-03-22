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
    url_scraping = 'https://www.niceprice62.ru/audio-video/audio/naushniki/'
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
        name = block.select_one('.list_name').get_text().strip()
        data['name'] = name

        image_url = block.select_one('a')
        data['image_url'] = 'https://www.niceprice62.ru/' + re.search(r'data-src=".+"\s{1}',
                                      str(image_url)).group().strip('data-src="').replace('"', '').split()[0]

        data['image_url'] = re.sub('jpe?g', 'webp', data['image_url'])

        if block.select_one('.old-price'):
            price_raw = block.select_one('.old-price').text
            price_raw = Decimal(''.join(re.findall(r'\d+', price_raw)))
            data['price'] = price_raw
        elif block.select_one('.list-price'):
            price_raw = block.select_one('.list-price').text
            price_raw = Decimal(''.join(re.findall(r'\d+', price_raw)))
            data['price'] = price_raw

        url_detailed = block.select_one('.list-td-image').select_one('a')['href']
        url_detailed = 'https://www.niceprice62.ru/' + url_detailed

        html_detailed = requests.get(url_detailed).text
        soup = BeautifulSoup(html_detailed, 'html.parser')
        code_block = soup.select_one('.container.main')
        code = code_block.select_one('.table-haract').get_text(separator='/n')

        data['description'] = code

        data_list.append(data)

    for dictionary in data_list:
        dict_name = dictionary['name']
        print(dictionary['description'])
        if not Product.objects.filter(name=dictionary['name']).exists():
            Product.objects.create(
                name=dictionary['name'],
                description=dictionary['description'],
                price=dictionary['price'],
                image_url=dictionary['image_url'],
                category=ProductCategory(id=3),
            )


if __name__ == '__main__':
    scraping()