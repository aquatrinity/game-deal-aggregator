# 🎮 Game Deal Aggregator

Streamlit app to search and compare game availability across:
- ✅ Paid stores (Steam, GOG via CheapShark API)
- 🧲 Torrents (1337x.to live scraping)
- 🕹️ Emulator ROM providers (CoolROM, RomsGames)

---

## 🔥 Features

- 🔎 **Smart Game Search** with Paid / Free / Torrent filters
- 🧠 Wikipedia-based related games with summaries
- 🎬 Embedded YouTube trailers (for top & paid games)
- 📈 Trending searches & top genres (RPG, Action, Sim)
- 🧾 Local search history with user login mock

---

## 🌐 Real-time Data Sources

| Source      | Type        | Notes                         |
|-------------|-------------|-------------------------------|
| CheapShark  | Paid games  | Steam, GOG, etc. via API      |
| 1337x.to    | Torrents    | Live scraped results          |
| CoolROM     | ROMs        | Emulator sites                |
| RomsGames   | ROMs        | Emulator ROM site             |
| Wikipedia   | Related     | Game suggestions              |
| YouTube     | Trailer     | Embed via search iframe       |

---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

## 📂 Files

```
.
├── streamlit_app.py           # UI logic and visuals
├── game_deal_aggregator.py    # Web scraping and APIs
├── requirements.txt
└── README.md
```
