pip install selenium pandas
import requests
import pandas as pd
import json

# Configuration
base_url = "https://api.coingecko.com/api/v3/coins/markets"
vs_currency = 'usd'
coins_per_page = 100  # max = 250
max_pages = 5         # donc 5 * 100 = 500 coins

cryptos = []

for page in range(1, max_pages + 1):
    params = {
        'vs_currency': vs_currency,
        'order': 'market_cap_desc',
        'per_page': coins_per_page,
        'page': page,
        'sparkline': False
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        for coin in data:
            cryptos.append({
                'name': coin['name'],
                'symbol': coin['symbol'],
                'current_price': coin['current_price'],
                'market_cap': coin['market_cap'],
                'total_volume': coin['total_volume'],
                'price_change_24h_%': coin['price_change_percentage_24h']
            })
    else:
        print(f" Erreur sur la page {page} : {response.status_code}")
        break

# Export JSON
with open('cryptos_500.json', 'w', encoding='utf-8') as f:
    json.dump(cryptos, f, indent=4, ensure_ascii=False)

# Export CSV
df = pd.DataFrame(cryptos)
df.to_csv('cryptos_500.csv', index=False, encoding='utf-8')

print(f" {len(cryptos)} cryptos exportées avec succès")
