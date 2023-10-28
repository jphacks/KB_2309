import sqlite3
import hashlib
import time

# SQLiteデータベースに接続
conn = sqlite3.connect('./database/database.db')

# カーソルを取得
cur = conn.cursor()

# テーブルの作成
cur.execute('''CREATE TABLE IF NOT EXISTS access (
    id TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)''')

cur.execute('''CREATE TABLE IF NOT EXISTS side_photos (
    access_id TEXT,
    back_arg float,
    leg_arg float,
    file_path TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    foreign key(access_id) references access(id)
)''')

cur.close()

