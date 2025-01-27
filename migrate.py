import sqlite3

conn = sqlite3.connect("pokemon.db")

cur = conn.cursor()

try:
    cur.execute(
        """CREATE TABLE pokemon (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        picture TEXT,
        name TEXT,
        ptype TEXT,
        total TEXT,
        hp TEXT,
        attack TEXT,
        defense TEXT,
        sp_attack TEXT,
        sp_defense TEXT,
        speed TEXT
    )"""
    )
    conn.commit()
except sqlite3.OperationalError as e:
    print(e)

conn.close()
