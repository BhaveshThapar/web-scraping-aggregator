import requests
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_yelp_menus(api_key, location="New York City", term="restaurants"):
    url = "https://api.yelp.com/v3/businesses/search"
    headers = {"Authorization": f"Bearer {api_key}"}
    params = {"location": location, "term": term, "limit": 50}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        businesses = response.json().get('businesses', [])
        menus = []
        for business in businesses:
            menus.append({ "name": business['name'], "address": ", ".join(business['location']['display_address']), "url": business.get('url', "N/A") })
        return menus
    else:
        print("Error:", response.status_code, response.text)
        return []

def print_menus(menus):
    for idx, menu in enumerate(menus, start=1):
        print(f"Restaurant {idx}:")
        print(f"  Name    : {menu['name']}")
        print(f"  Address : {menu['address']}")
        print(f"  URL     : {menu['url']}")
        print("-" * 40)

YELP_API_KEY = os.getenv("YELP_API_KEY")

if YELP_API_KEY:
    yelp_menus = fetch_yelp_menus(YELP_API_KEY)
    print_menus(yelp_menus)
else:
    print("Error: YELP_API_KEY is not set in the environment.")