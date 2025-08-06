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
    title = soup.find("span", {"class": "B_NuCI"}).text.strip()
    price = soup.find("div", {"class": "_30jeq3 _16Jk6d"}).text.strip()
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
        "https://www.flipkart.com/as-it-is-nutrition-atom-whey-protein/p/itm7e172d65e6c39?pid=PSLGFZ7TAHXRHUTX&lid=LSTPSLGFZ7TAHXRHUTXDWA86G&marketplace=FLIPKART&q=asitis%20protein%20powder&sattr[]=quantity&sattr[]=flavor&st=flavor",
        "https://www.flipkart.com/tata-1mg-magnesium-glycinate-tablets-muscle-recovery-sleep-nerve-health/p/itmb5e128d34e67f?pid=VSLHACV4AFCDWNGG&lid=LSTVSLHACV4AFCDWNGGIPD1ZI&marketplace=FLIPKART&q=tata+1mg+magnesium+glycinate&store=hlc%2Fetg%2Fqtw&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_ps&fm=search-autosuggest&iid=en_JJWTYUPZ1LYajSqj-T05v-fSrG9rV0aJyq_XDgovxny5Oicj5buZk_zZ255he5xqpkEiT0zGzRhmvMRudN3ZIPUFjCTyOHoHZs-Z5_PS_w0%3D&ppt=sp&ppn=sp&ssid=rk5pdyo2pc0000001754465654252&qH=16390498ca0676e8"
    ]
    for url in urls:
        title, price = get_price(url)
        send_whatsapp(title, price)
