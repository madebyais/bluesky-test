from dotenv import load_dotenv

load_dotenv()

import sqlite3

from resources.database import Database

print("[MIGRATE] Migrating data ...")

try:
    db = Database().session()

    cur = db.cursor()
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

    db.commit()
    db.close()
except sqlite3.OperationalError as e:
    print("[MIGRATE] Migrating data ... ERROR")
    print(f"[MIGRATE] Error: {str(e)}")


print("[MIGRATE] Migrating data ... DONE")
