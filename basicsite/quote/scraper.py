import requests
from bs4 import BeautifulSoup as BS
import re

def scrape_price(part_number, brand):
    url = f'https://www.electronshik.ru/search?query={part_number}&in_stock=1&view=table'
    r = requests.get(url)
    soup = BS(r.text, 'lxml')
    try:
        for i, item in enumerate(soup.find_all('tr', class_='product-row')):
            c_pn = item.find('a', class_='part-name').text
            c_pn = re.sub(r'\(.*\)', '', c_pn).strip()
            c_b = item.find('span', class_='part-producer').text.strip()
            #print(f'{i}: {c_pn} - {c_b}')
            if c_pn == part_number and c_b == brand:
                try:
                    quantity = item.find('span', class_='part-qty').text.strip()
                except:
                    quantitu = '0'
                try:
                    integer = item.find('span', class_='integer').text
                    fraction = item.find('span', class_='fraction').text
                    return str(float((integer + fraction).replace(',', '.'))) + ' / ' + quantity
                except:
                    return 'Нет данных'
    except:
        return 'Нет данных'