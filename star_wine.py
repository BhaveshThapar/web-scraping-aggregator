import requests
from bs4 import BeautifulSoup


def fetch_all_wine_lists(base_url="https://starwinelist.com/wine-lists/new-york-city"):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    wine_lists = []
    page = 1

    while True:
        url = f"{base_url}?page={page}"

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print("Error:", response.status_code, response.text)
            break

        soup = BeautifulSoup(response.text, "html.parser")
        page_wine_lists = []

        for item in soup.select("li.producers-page__list-item"):
            link = item.select_one("a.producers-page__list-item-link")
            location = item.select_one("span")
            if link:
                page_wine_lists.append({
                    "name": link.text.strip(),
                    "location": location.text.strip() if location else "No location available",
                    "url": link['href']
                })

        if not page_wine_lists:
            break

        wine_lists.extend(page_wine_lists)
        page += 1

    return wine_lists


def print_wine_lists(wine_lists):
    for idx, wine in enumerate(wine_lists, start=1):
        print(f"Wine List {idx}:")
        print(f"  Name     : {wine['name']}")
        print(f"  Location : {wine['location']}")
        print(f"  URL      : {wine['url']}")
        print("-" * 50)


wine_lists = fetch_all_wine_lists("https://starwinelist.com/wine-lists/new-york-city")
print_wine_lists(wine_lists)
