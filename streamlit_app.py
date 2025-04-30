# file: streamlit_app.py

import streamlit as st
import sqlite3
from collections import Counter
import pandas as pd
from datetime import datetime
from game_deal_aggregator import init_db, search_game, CACHE_DB
import webbrowser
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

init_db()

# Add user search table
with sqlite3.connect(CACHE_DB) as conn:
    conn.execute("""
    CREATE TABLE IF NOT EXISTS searches (
        id INTEGER PRIMARY KEY,
        username TEXT,
        game TEXT,
        timestamp DATETIME
    )
    """)

st.set_page_config(page_title="Game Deal Aggregator", layout="wide")
st.title("🎮 Game Deal Aggregator")

st.warning("""
📜 **Disclaimer**: This app is for educational and research purposes only.
You are solely responsible for how you use the data.
Respect all copyright and piracy laws in your region.
""")

# --- User login mock (simple session auth) ---
if 'user' not in st.session_state:
    st.session_state.user = None

if not st.session_state.user:
    with st.form("Login"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        if submit:
            if username and password:
                st.session_state.user = username
            else:
                st.error("Username and password required")
        st.stop()

st.success(f"Welcome {st.session_state.user}!")

# --- Sidebar: User History ---
st.sidebar.header("🕓 Your Recent Searches")
with sqlite3.connect(CACHE_DB) as conn:
    rows = conn.execute("SELECT DISTINCT game FROM searches WHERE username = ? ORDER BY timestamp DESC LIMIT 5", (st.session_state.user,)).fetchall()
    for (g,) in rows:
        st.sidebar.markdown(f"- {g}")

# --- Trending ---
st.subheader("🔥 Trending Searches")
with sqlite3.connect(CACHE_DB) as conn:
    rows = conn.execute("SELECT game FROM searches").fetchall()
    counter = Counter(title for (title,) in rows)
    for title, count in counter.most_common(5):
        st.markdown(f"- **{title}** ({count} searches)")

# --- ROM scrapers ---
def search_rom_vimms(game):
    results = []
    url = f"https://vimm.net/vault/?p=list&q={quote_plus(game)}"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, 'html.parser')
    for row in soup.select("table.list tr")[1:6]:
        cols = row.find_all('td')
        if len(cols) >= 3:
            title = cols[0].get_text(strip=True)
            platform = cols[1].get_text(strip=True)
            link_tag = cols[0].find('a')
            if link_tag and link_tag['href']:
                link = f"https://vimm.net{link_tag['href']}"
                results.append({
                    'title': title,
                    'source': "Vimm's Lair",
                    'price': 'Free (ROM)',
                    'link': link,
                    'image': '',
                    'description': f"ROM for {platform}"
                })
    return results

def search_rom_coolrom(game):
    results = []
    url = f"https://coolrom.com/search?q={quote_plus(game)}"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, 'html.parser')
    for row in soup.select(".gamelist li")[:5]:
        a = row.find('a')
        if a:
            title = a.get_text(strip=True)
            link = f"https://coolrom.com{a['href']}"
            results.append({
                'title': title,
                'source': "CoolROM",
                'price': 'Free (ROM)',
                'link': link,
                'image': '',
                'description': 'ROM listing from CoolROM'
            })
    return results

def search_rom_romsgames(game):
    results = []
    url = f"https://www.romsgames.net/?s={quote_plus(game)}"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, 'html.parser')
    for post in soup.select(".entry-title a")[:5]:
        title = post.get_text(strip=True)
        link = post['href']
        results.append({
            'title': title,
            'source': "RomsGames",
            'price': 'Free (ROM)',
            'link': link,
            'image': '',
            'description': 'ROM post from RomsGames.net'
        })
    return results

# --- Game search ---
st.subheader("🔎 Search a Game")
game = st.text_input("Enter a game title")
filter_option = st.selectbox("Filter by", ["All", "Paid", "Free", "Torrent"])
sort_option = st.selectbox("Sort by", ["Default", "Price (asc)", "Source"])

if st.button("Search") and game:
    # Save search to DB
    with sqlite3.connect(CACHE_DB) as conn:
        conn.execute("INSERT INTO searches (username, game, timestamp) VALUES (?, ?, ?)", (st.session_state.user, game, datetime.utcnow()))

    data = search_game(game)
        data += search_rom_romsgames(game)

    # Filter logic
    if filter_option == "Paid":
        data = [d for d in data if 'Paid' in d['description']]
    elif filter_option == "Free":
        data = [d for d in data if 'Free' in d['price']]
    elif filter_option == "Torrent":
        data = [d for d in data if 'Torrent' in d['price']]

    # Sort logic
    if sort_option == "Price (asc)":
        def parse_price(p):
            try:
                return float(p.strip('$'))
            except:
                return float('inf')
        data.sort(key=lambda x: parse_price(x['price']))
    elif sort_option == "Source":
        data.sort(key=lambda x: x['source'])

    # Display
    st.write(f"### Results for '{game}' ({len(data)} found)")
    for d in data:
        with st.container():
            st.markdown(f"**{d['title']}**")
            st.image(d['image'], width=150) if d['image'] else None
            st.markdown(f"`{d['price']}` — *{d['source']}*")
            st.markdown(f"{d['description'][:200]}...")
            if st.button(f"🔗 Open in new tab: {d['source']}", key=d['link']):
                webbrowser.open_new_tab(d['link'])
            st.markdown("---")
