import requests
from bs4 import BeautifulSoup

def fetch_products_prices(url):

    resp = requests.get(url)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, 'html.parser')

    product_dict = {}

    for item in soup.select('.products product_list   waypoint  row grid   clear_list_18'
                            '  clear_list_align_0 clear_list_proportion_0'):
        title_tag = item.find('flex_box flex_start mini_name')
        price_tag = item.find(string=lambda t: 'تومان' in t if t else False)
        print(title_tag)
        if title_tag and price_tag:
            title = title_tag.get_text(strip=True)
            price = price_tag.strip()
            product_dict[title] = price

    return product_dict


get_url = 'https://iphonechi.com/21-macbook-air'
products = fetch_products_prices(get_url)

for product, product_price in products.items():
    print(f"{product}: {product_price}")
