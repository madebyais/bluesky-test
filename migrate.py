import sqlite3

print("[MIGRATE] Migrating data ...")

conn = sqlite3.connect("pokemon.db")

cur = conn.cursor()

try:
    cur.execute(
        """CREATE TABLE pokemon (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_id TEXT,
        picture TEXT,
        name TEXT,
        ptype TEXT,
        total INTEGER,
        hp INTEGER,
        attack INTEGER,
        defense INTEGER,
        sp_attack INTEGER,
        sp_defense INTEGER,
        speed INTEGER
    )"""
    )
    conn.commit()
except sqlite3.OperationalError as e:
    print("[MIGRATE] Migrating data ... ERROR")
    print(f"[MIGRATE] Error: {str(e)}")

conn.close()

print("[MIGRATE] Migrating data ... DONE")