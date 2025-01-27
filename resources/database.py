import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("pokemon.db")

    def session(self):
        return self.conn
