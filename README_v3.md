# 🎮 Game Deal Aggregator (v3.0)

A powerful full-stack app to find PC game deals and links across:
- ✅ Paid platforms
- 🧲 Torrents
- 🕹️ ROM and repack sites

---

## 🔥 What's New (v3.0)

- 🚀 Real-time data from:
  - CheapShark API (Steam, GOG, etc.)
  - 1337x.to (Torrent search)
  - 16 popular repack blogs
- 🎮 Game genre lookup via Steam search
- 🧠 Smart Wikipedia links & related games
- 🎬 Embedded YouTube trailers
- 🗂️ Local SQLite cache
- 🔍 CLI & Streamlit UI both available

---

## 🧠 Features

| Feature         | Description                                      |
|-----------------|--------------------------------------------------|
| Smart search    | Unified results across free, paid, torrent games |
| Genre tag       | Uses DuckDuckGo + Steam for accurate genres      |
| Filters         | Paid, Free, Torrent, All                         |
| Cover Art       | SteamGridDB placeholder or site thumbnails       |
| Caching         | Results saved for fast future lookup             |
| Related games   | Wikipedia-based suggestions                      |
| Trailer         | YouTube iframe embed (paid/top genre)           |

---

## 🛠 Tech Stack

- Python, Streamlit
- BeautifulSoup, Requests
- SQLite cache
- DuckDuckGo scraping
- CheapShark API

---

## 🧪 Usage (CLI)

```bash
python game_deal_aggregator.py
```

---

## 🌐 Web App (Streamlit)

```bash
streamlit run streamlit_app.py
```

---

## 📂 Project Structure

```
.
├── streamlit_app.py           # Streamlit interface
├── game_deal_aggregator.py    # Data fetcher + CLI mode
├── requirements.txt
└── README.md
```

---

## 📜 Disclaimer

> This app is for educational and research purposes only.  
> The author is not responsible for how this is used.  
> Respect copyright laws in your region.

