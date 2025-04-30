# 🎮 Game Deal Aggregator (v3.1 - Live Search)

An intelligent multi-source app to find real-time PC game deals and downloads from:

- ✅ Paid platforms (Steam, GOG via CheapShark)
- 🧲 Torrent indexes (1337x)
- 🎁 Repack groups (FitGirl, DODI, ElAmigos, etc.)

---

## 🔥 New in v3.1

- 🧠 **Live title suggestions** from SQLite cache (top 500 recent searches)
- 🔎 Auto-filter out placeholder/sample data
- 📊 Filter by price: Free / Paid / Torrent
- 🧩 Sort by: Source or Price
- 📂 Cleaned layout with left/right search controls

---

## 💡 Features

| Category      | Description                                     |
|---------------|-------------------------------------------------|
| Search        | Real-time scraping from store, torrent, repack  |
| Filtering     | Paid / Free / Torrent toggle                    |
| Sorting       | Source, Price (Low→High or High→Low)            |
| Suggestions   | Auto-filled dropdown from real titles cached    |
| UI            | Streamlit + SQLite-backed system                |

---

## 🛠 Stack

- Python + Streamlit
- CheapShark API
- BeautifulSoup (repack/torrent scrapers)
- SQLite for caching
- Wikipedia (related), YouTube (trailers)

---

## 🚀 Launch

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

## 📁 Project Structure

```
.
├── streamlit_app.py           # UI + visuals
├── game_deal_aggregator.py    # Data engine + scrapers
├── requirements.txt
└── README.md
```

---

## ⚠️ Legal

> This project is for **research & educational purposes only**.  
> You are responsible for how you use it.  
> Follow copyright laws in your region.

