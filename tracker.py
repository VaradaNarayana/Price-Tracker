import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import os

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 11)"
}

def get_price(url):
    r = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(r.content, "html.parser")

    # Extract product title
    title_tag = soup.find("h1")
    title = title_tag.text.strip() if title_tag else "❌ Title not found"

    # Extract Flipkart price
    price_block = soup.find("div", class_="card border-info mb-3")
    price_tag = price_block.find("h4") if price_block else None
    price = price_tag.text.strip() if price_tag else "❌ Price not found"

    return title, price



def send_whatsapp(product, price):
    client = Client(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])
    message = client.messages.create(
        body=f"{product}\nPrice: {price}",
        from_="whatsapp:+14155238886",
        to="whatsapp:+917996261245"
    )
    print("Sent:", message.sid)

if __name__ == "__main__":
    urls = [
        "https://price-history.in/product/nutrition-atom-whey-protein-isolate-1kg-NP9zkAyp",
        "https://price-history.in/product/tata-1mg-magnesium-glycinate-tablets-muscle-OM0Zipmb"
    ]
    for url in urls:
        title, price = get_price(url)
        send_whatsapp(title, price)
