import sqlite3
import hashlib
import time

database_path = './database/database.db'

# Accessの追加 (Create)
def create_access(id):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute("INSERT INTO access (id) VALUES (?)", (id,))
    cur.close()
    
def create_side_photo(access_id, back_arg, leg_arg, file_path):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute("INSERT INTO side_photos (access_id, back_arg, leg_arg, file_path) VALUES (?,?,?,?)", (access_id, back_arg, leg_arg, file_path,))    
    cur.close()
    
def create_front_photo(access_id, xxx_arg, yyyy_arg, file_path):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute("INSERT INTO front_photos (access_id, xxx_arg, yyyy_arg, file_path) VALUES (?,?,?,?)", (access_id, xxx_arg, yyyy_arg, file_path,))
    cur.close()

# Accessの取得 (Read)
def get_access_by_id(id):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM access WHERE id=?", (id,))
    access = cur.fetchone()
    cur.close()
    return access
    
def get_photos_by_access_id(access_id):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM side_photos WHERE access_id=?", (access_id,))
    side_photos = cur.fetchall()
    cur.execute("SELECT * FROM front_photos WHERE access_id=?", (access_id,))
    front_photos = cur.fetchall()
    cur.close()
    return side_photos, front_photos

