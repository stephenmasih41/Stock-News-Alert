# 🚀📈 Stock News Alert  
### 🐍 Day 36 of My Python Bootcamp Journey  

Welcome to **Day 36** of my Python Bootcamp project! 🎯  
This project automatically monitors **Tesla’s stock price (TSLA)** using real-time data from the **Alpha Vantage API**.  

If Tesla’s stock price changes by **more than 5%**, the program will:  
📰 Fetch the latest **top 3 news articles** about Tesla from the **News API**  
📧 Send them straight to your **email inbox** using **SMTP** (Gmail)  

Simple, smart, and perfect for automating financial updates! 💼⚙️  

---

## ✨ Features

✅ **Daily Stock Tracking** — Fetches Tesla’s most recent trading data 📊  
✅ **Automatic Price Change Detection** — Checks if the stock moved more than 5% 📉📈  
✅ **News Integration** — Pulls the top 3 latest and most popular Tesla news articles 🗞️  
✅ **Email Notifications** — Sends updates directly to your email inbox 💌  
✅ **Emoji Included** — Because data should be fun 😄  

---

## 🧰 Tech Stack & Tools

| 🧩 Tool / Library | 🧠 Purpose |
|-------------------|------------|
| `requests` | Fetches stock and news data via APIs 🌐 |
| `smtplib` | Sends email notifications securely via Gmail ✉️ |
| `Alpha Vantage API` | Provides Tesla stock data 📈 |
| `News API` | Supplies Tesla-related news 📰 |
| `Python 3` | The language powering everything 🐍 |

---

## ⚙️ How It Works

1. 📡 The script requests **Tesla’s stock data** from the **Alpha Vantage API**.  
2. 🧮 It compares **yesterday’s closing price** with the **day before yesterday’s**.  
3. 📊 If the price difference is **greater than 5%**, the script:  
   - Retrieves the **latest Tesla news** using the **News API**.  
   - Formats an email including:
     - 📈 Stock movement (🔺 up or 🔻 down)  
     - 📰 Top 3 news headlines and summaries  
   - Sends the email using **SMTP** through **Gmail**.  

---

## 🧩 Example Output (Email Preview)

```
Subject: TSLA: 🔺6.32%

Headline: Tesla shares surge after strong quarterly earnings  
Brief: Tesla’s Q3 results exceeded Wall Street expectations, pushing the stock up by over 6% in one day.

Headline: Elon Musk hints at next-gen Tesla model  
Brief: The CEO revealed that Tesla is working on a new affordable EV during the earnings call.
```

---

## 🧠 Code Breakdown

### 🧾 1. Importing Modules
```python
import requests
import smtplib
```

### 🧱 2. Setting Constants
Define:
- Stock name (`TSLA`)
- Company name (`Tesla Inc`)
- API endpoints & keys 🔑
- Email credentials 📧

### 📊 3. Fetching Stock Data
```python
stocks = requests.get(STOCK_ENDPOINT, params=stock_dict)
stocks_data = stocks.json()['Time Series (Daily)']
```

### 🔢 4. Calculating Price Difference
```python
difference = abs(yesterday_stock_price - before_yesterday_stock_price)
percentage_difference = round((difference / float(before_yesterday_stock_price)) * 100, 2)
```

### 📨 5. Fetching and Sending News
```python
if percentage_difference > 5:
    # Fetch top 3 news
    # Send email via SMTP
```

---

## 🔐 Security & API Setup

To make this work securely, you’ll need your **own API keys** and **email credentials**.  

### 🔑 Replace These:
- `my_email` → Your Gmail address  
- `password` → Your **App Password** (not your real password!)  
- `to_addrs` → The recipient email  

### 🧭 Gmail App Password Setup:
1. Go to your [Google Account Security Settings](https://myaccount.google.com/security)  
2. Enable **2-Step Verification**  
3. Generate a new **App Password** for “Mail”  
4. Use that password in this script ✅  

---

## 🌐 APIs Used

1. 🔹 **Alpha Vantage API** — for real-time Tesla stock prices  
2. 🔹 **News API** — for current Tesla-related news  

Both are **free to use** (just sign up to get your own API keys).  

---

## 🌟 What I Learned

✅ Working with **real-world APIs**  
✅ Parsing complex **JSON data**  
✅ Using **f-strings** for clean message formatting  
✅ Sending **automated emails** securely  
✅ Building a **real automation tool** from scratch  

---

