import os, sqlite3


def get_db():
    conn = sqlite3.connect(os.getenv("DATABASE_FILEPATH"))
    try:
        yield conn
    finally:
        conn.close()


class Database:
    def __init__(self):
        pass

    def session(self):
        conn = sqlite3.connect(os.getenv("DATABASE_FILEPATH"))
        return conn
