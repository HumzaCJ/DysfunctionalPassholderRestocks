import time
import requests
import tls_client

session = tls_client.Session(client_identifier="chrome_120", random_tls_extension_order=True)

WEBHOOK_URL = 'REPLACE WITH YOUR DISCORD WEBHOOK'
API_URL = 'https://www.dysfunctionalpassholder.com/api/commerce/inventory/stock/'
ITEM_ID = '680505605a30552faf81f22a'

was_in_stock = False

def send_webhook(qty):
    title = "Pokenot Fundle Bundle Box - 8 Booster per box"
    query = title.replace(' ', '+')
    requests.post(WEBHOOK_URL, json={
        "embeds": [{
            "title": f"{title}",
            "url": "https://www.dysfunctionalpassholder.com/trading-cards-97/p/ghuids5",
            "thumbnail": {"url": "https://images.squarespace-cdn.com/content/v1/65170e065ab5332f648ed173/76080e98-434b-406d-9c72-5c19c053d89a/1.png?format=750w"},
            "color": 0x800080,
            "footer": {"text": "Powered By Lunar FBA"},
            "fields": [
                {"name": "Price", "value": "$65.00", "inline": True},
                {"name": "Stock", "value": str(qty), "inline": True},
                {
                    "name": "Marketplace Links",
                    "value": f"[eBay Active](https://www.ebay.co.uk/sch/i.html?_nkw={query}&_sacat=0) | [eBay Sold](https://www.ebay.co.uk/sch/i.html?_nkw={query}&_sacat=0&LH_Complete=1&LH_Sold=1)",
                    "inline": False
                }
            ]
        }]
    })

def check_stock():
    global was_in_stock
    try:
        res = session.get(API_URL, params={'itemId': ITEM_ID})
        data = res.json()
        qty = data["results"][0].get("qtyInStock", 0) if data["results"] else 0

        if qty > 0 and not was_in_stock:
            send_webhook(qty)
            was_in_stock = True
        elif qty == 0:
            was_in_stock = False
    except Exception as e:
        print(f"Error: {e}")

while True:
    check_stock()
    time.sleep(2)
