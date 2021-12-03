import requests
from bs4 import BeautifulSoup
import json

def get_data(url):
    hdr = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        "Accept-language": "fr, en",
    }
    r = requests.get(url, headers=hdr)
    soup = BeautifulSoup(r.text, "html.parser").find("script", type="application/ld+json")
    product_data = json.loads(soup.string)
    name = product_data['name']
    price_endpoint = f"https://www.asos.com/api/product/catalogue/v3/stockprice?productIds={product_data['productID']}&store=FR&currency=EUR"
    price = float(requests.get(price_endpoint, headers=hdr).json()[0]['productPrice']['current']['text'][:-2].replace(",", "."))

    return name, price

