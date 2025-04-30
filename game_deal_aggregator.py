
# file: game_deal_aggregator.py

import sqlite3
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from datetime import datetime

CACHE_DB = "game_cache.db"

def init_db():
    with sqlite3.connect(CACHE_DB) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY,
            title TEXT,
            source TEXT,
            price TEXT,
            link TEXT,
            image TEXT,
            description TEXT,
            timestamp DATETIME
        )
        """)

def search_game(game):
    # Sample static return for deployment test
    return [{
        'title': game,
        'source': 'CheapShark',
        'price': '$14.99',
        'link': 'https://www.cheapshark.com/',
        'image': '',
        'description': f'{game} deal via CheapShark'
    }]
