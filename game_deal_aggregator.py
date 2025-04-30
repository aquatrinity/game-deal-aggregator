
# file: game_deal_aggregator.py

import sqlite3
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
        )""")

def search_game(game):
    return [{
        'title': game,
        'source': 'Sample Source',
        'price': '$4.99',
        'link': 'https://example.com',
        'image': '',
        'description': 'Sample result'
    }]
