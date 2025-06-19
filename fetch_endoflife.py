import json
import requests
from pathlib import Path

CONFIG_FILE = Path("products.json")
OUTPUT_FILE = Path("endoflife.json")
BASE_URL = "https://endoflife.date/api/v1/products/{}"

def load_products():
    with open(CONFIG_FILE) as f:
        return json.load(f)

def fetch_product_data(product):
    url = BASE_URL.format(product)
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def main():
    if not CONFIG_FILE.exists():
        raise FileNotFoundError(f"Konfigurationsdatei nicht gefunden: {CONFIG_FILE}")
    
    products = load_products()
    result = {}

    for product in products:
        try:
            print(f"Fetching: {product}")
            result[product] = fetch_product_data(product)
        except Exception as e:
            print(f"❌ Fehler bei {product}: {e}")

    with open(OUTPUT_FILE, "w") as f:
        json.dump(result, f, indent=2)
        print(f"✅ Daten gespeichert in {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
