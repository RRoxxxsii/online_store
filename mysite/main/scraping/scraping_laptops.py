import re
import requests
from _decimal import Decimal
from bs4 import BeautifulSoup
from scraping_errors import *


def scraping():
    URL_SCRAPING = 'https://www.niceprice62.ru/noutbuki-i-kompjuternaja-tehnika/noutbuki/'
    try:
        resp = requests.get(URL_SCRAPING, timeout=10.0)
    except requests.exceptions.Timeout:
        raise ScrapingTimeoutError("request timed out")
    except Exception as e:
        raise ScrapingOtherError(f'{e}')

    if resp.status_code != 200:
        raise ScrapingHTTPError(f"HTTP {resp.status_code}: {resp.text}")

    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')
    blocks = soup.select('.list-tr')
    for block in blocks:
        data = {}
        name = block.select_one('.list-td-name').get_text().strip()
        data['name'] = name

        image_url = URL_SCRAPING + block.select_one('img')['src']
        data['image_url'] = image_url

        price_raw = block.select_one('.list-price').text
        price_raw = Decimal(''.join(re.findall('\d{1,}', price_raw)))
        data['price'] = price_raw

        print(data)

if __name__ == '__main__':
    scraping()

