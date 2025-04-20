import pandas as pd
import numpy as np

# Charger les données JSON
with open('../cryptos_with_problems.json', 'r', encoding='utf-8') as f:
    cryptos = json.load(f)

# Convertir en DataFrame
df = pd.DataFrame(cryptos)

# 1. Vérification des doublons
print("Nombre de doublons avant suppression:", df.duplicated().sum())
df = df.drop_duplicates()  # Supprimer les doublons
print("Nombre de doublons après suppression:", df.duplicated().sum())

# 2. Vérification des valeurs manquantes (NaN)
print("Valeurs manquantes avant traitement:")
print(df.isnull().sum())

# Imputer les valeurs manquantes (par la moyenne dans ce cas)
df['current_price'] = df['current_price'].fillna(df['current_price'].mean())
df['market_cap'] = df['market_cap'].fillna(df['market_cap'].mean())
df['total_volume'] = df['total_volume'].fillna(df['total_volume'].mean())
df['price_change_24h_%'] = df['price_change_24h_%'].fillna(df['price_change_24h_%'].mean())

print("Valeurs manquantes après traitement:")
print(df.isnull().sum())

# 3. Vérification des valeurs aberrantes : ici, on peut supposer qu'un prix ou une capitalisation négatifs sont des anomalies
print("Vérification des valeurs négatives dans 'current_price' :")
print(df[df['current_price'] < 0])

# Remplacer les prix négatifs par la moyenne des prix
df['current_price'] = df['current_price'].apply(lambda x: x if x >= 0 else df['current_price'].mean())

# 4. Vérification des valeurs aberrantes pour la capitalisation boursière
print("Vérification des valeurs aberrantes dans 'market_cap' :")
print(df[df['market_cap'] < 0])

# Remplacer les capitalisations boursières négatives par la moyenne des capitalisations
df['market_cap'] = df['market_cap'].apply(lambda x: x if x >= 0 else df['market_cap'].mean())

# 5. Vérification des outliers : Utilisation de l'écart interquartile (IQR)
Q1 = df['price_change_24h_%'].quantile(0.25)
Q3 = df['price_change_24h_%'].quantile(0.75)
IQR = Q3 - Q1

# Détection des outliers
outliers = df[(df['price_change_24h_%'] < (Q1 - 1.5 * IQR)) | (df['price_change_24h_%'] > (Q3 + 1.5 * IQR))]
print(f"Nombre d'outliers détectés dans 'price_change_24h_%': {len(outliers)}")

# Supprimer les outliers
df = df[~df['price_change_24h_%'].isin(outliers['price_change_24h_%'])]

# 6. Enregistrer les données prétraitées dans un nouveau fichier JSON
with open('cryptos_preprocessed.json', 'w', encoding='utf-8') as f:
    json.dump(df.to_dict(orient='records'), f, indent=4, ensure_ascii=False)

# 7. Enregistrer les données prétraitées dans un fichier CSV
df.to_csv('cryptos_preprocessed.csv', index=False, encoding='utf-8')

# Affichage des premières lignes des données après prétraitement
print("Données après prétraitement :")
print(df.head())

