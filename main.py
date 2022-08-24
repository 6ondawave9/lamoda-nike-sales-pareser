import requests
from bs4 import BeautifulSoup as bs
import json

URL_TEMPLATE = "https://www.lamoda.ru/c/5971/shoes-muzhkrossovki/?zbs_content=js_m_icons_869376_ru_070422_icon_m_ss22&is_sale=1&sort=price_asc&brands=2047"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
r = requests.get(URL_TEMPLATE, headers=headers)
print(r.status_code)
data = r.text

file = open(r"C:\Users\Работа\Desktop\\nike_sale.txt", "w", encoding="utf-8")

soup = bs(r.text, "html.parser")
all_cards = soup.find_all('div', class_='x-product-card__card')
for card in all_cards:

    name = card.find('div', class_='x-product-card-description__product-name').text
    name = name[1:]

    price = card.find('span', class_='x-product-card-description__price-new').text
    price = price[:-1].replace(" ", "")

    old_price = card.find('span', class_='x-product-card-description__price-old').text

    sale = (int(old_price.replace(" ", ""))) - int(price)
    if sale>5000:
        sale = f"{str(sale)} !!!!!!!!!!!!!!"

    file.write(f"{name} - {price} P - {sale} P\n\n")

print("done")