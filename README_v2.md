# 🎮 Game Deal Aggregator

Streamlit app to search and compare game availability across:
- ✅ Paid sources (Steam, GOG, etc.)
- 🎁 Free and cracked repack sites
- 🧲 Torrent trackers
- 🕹️ Emulator ROM providers

---

## 🔥 Features

- 🔎 **Smart Game Search** with filters (Paid, Free, Torrent)
- 📈 **Trending titles** with cover art
- 🧠 **Wikipedia related game links** + 1-line summaries
- 🎬 **YouTube trailer embed** for paid or top-genre games
- 🧾 Local cache history per user
- 📂 Top genres (RPG, Action, Sim) with visual showcase

---

## 🧠 Related Game & Trailer Insights

- Pulls related titles from **Wikipedia**
- Embeds a **YouTube trailer iframe** when it's a paid or top-listed game

---

## 📜 Disclaimer

> This tool is for research and educational purposes only.  
> You are fully responsible for its use.  
> Respect copyright laws in your region.

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

## 🧰 Tech Stack

- Python
- Streamlit
- BeautifulSoup (for scraping)
- SQLite (for caching)
- Wikipedia & YouTube integrations

---

## 📁 Files

```
.
├── streamlit_app.py           # Full Streamlit UI
├── game_deal_aggregator.py    # Data & scraper logic
├── requirements.txt
└── README.md
```
