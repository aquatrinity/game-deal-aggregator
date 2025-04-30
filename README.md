# 🎮 Game Deal Aggregator

A Streamlit app that helps you search for games across:
- Paid platforms (Steam, GOG via CheapShark)
- Cracked/repacks (FitGirl, DODI, IGG, etc.)
- Torrents (1337x)
- ROMs for emulators (Vimm’s Lair, CoolROM, RomsGames)

---

## 🚀 Features

- 🔎 Game search + filters (paid, torrent, free)
- 📈 Trending search history
- 👤 User login with local search tracking
- 💾 Game genre and platform detection
- 🌐 External link buttons (open in browser)
- 💡 ROM site fallback logic (safe on Streamlit Cloud)

---

## 📜 Disclaimer

> This app is for **educational and research purposes only**.  
> Use responsibly. Respect all copyright and piracy laws.

---

## 🔄 Changelog

### `v2.0` (Latest)
- ✅ ROM site scrapers added: Vimm's Lair, CoolROM, RomsGames
- ✅ SSL fallback for restricted Cloud environments
- ✅ Legal disclaimer warning on homepage
- ✅ New repo bundle with clean UI and filters

### `v1.0`
- Basic game search
- CheapShark API
- Torrent + repack scrapers
- SQLite local cache

---

## 🛠 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

## 🌍 How to Deploy (Streamlit Cloud)

1. Push this repo to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Set:
   - Repo: `your-name/game-deal-aggregator`
   - Branch: `main`
   - File: `streamlit_app.py`

---

## 📂 Repo Contents

```
.
├── streamlit_app.py           # UI + frontend
├── game_deal_aggregator.py    # Main scraper backend
├── requirements.txt           # Python packages
└── README.md                  # You’re here
```
