# 📈 Crypto Data Mining Project

## 🚀 Overview

The cryptocurrency market moves fast — being able to understand and anticipate trends is crucial for investors, analysts, and tech enthusiasts.  
This project delivers a complete **Data Mining pipeline** for crypto data using real-time information sourced via Selenium scraping from [CoinGecko](https://www.coingecko.com).  

We cover:

- 🔍 Real-time Web Scraping
- 🧹 Data Cleaning & Feature Engineering
- 📊 Exploratory Data Analysis (EDA)
- 🤖 Machine Learning (Classification & Regression)
- 📈 Model Performance Evaluation

---

## 🧰 Tech Stack

| Tool / Library     | Usage                                      |
|--------------------|---------------------------------------------|
| Python             | Core programming language                   |
| Selenium           | Web scraping automation                     |
| Pandas & NumPy     | Data manipulation and preprocessing         |
| Matplotlib & Seaborn | Data visualization (EDA & results)         |
| Scikit-learn       | ML models (Logistic Regression, RF, XGB)   |
| JSON               | Export format for clean data                |

---

## 📥 Data Collection

Data is scraped from **CoinGecko** and includes:

- Name of cryptocurrency
- Current price
- Price variation (1h, 24h)
- Market trend (derived feature)

📂 Output: `crypto_data_cleaned.json`

---

## 🧼 Data Preprocessing

Key steps include:

- Handling missing & outlier values
- Feature engineering (trend labeling: ↑, ↓, ↔)
- Normalization and type casting
- JSON export for modeling use

---

## 📊 Exploratory Data Analysis (EDA)

We explore and visualize:

- Distribution of price changes
- Correlation between crypto variables
- Top movers and most volatile coins
- Trends across multiple time windows

---

## 🔍 Supervised Machine Learning

### ✅ Classification  
**Goal**: Predict if a crypto will go **up**, **down**, or remain **stable** in the next hour/24h.

Models used:

- Logistic Regression  
- Random Forest Classifier  
- XGBoost  

Metrics:

- Accuracy, Precision, Recall, F1-score  
- Confusion Matrix  
- Visualizations using Pairplots  

---

### 📈 Regression  
**Goal**: Predict the **future price** of a given cryptocurrency.

Models tested:

- Linear Regression  
- Random Forest Regressor  
- XGBoost Regressor  

Metrics:

- RMSE (Root Mean Squared Error)  
- MAE (Mean Absolute Error)  
- R² (Coefficient of determination)

---

## 📌 Results Summary

All model results are compared and visualized using:

- Score tables (Pandas DataFrames)  
- Bar plots and heatmaps for model comparison  
- Feature importance visualizations  

---

## 🎯 Objective

This project offers:

- 📡 Real-time crypto trend detection
- 🧠 Predictive analytics for better decision making
- 💼 Tools for algorithmic trading, DeFi, and education in fintech

---

## 🔗 References

- [CoinGecko API Documentation](https://www.coingecko.com/en/api/documentation)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/user_guide.html)

---

