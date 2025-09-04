import sqlite3
import os


class BibleDB:
    def __init__(self, db_path="~/Documents/database/verses_bible.db"):
        self.db_path = os.path.expanduser(db_path)

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def table(self):
        with self.get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS verses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                 reference TEXT NOT NULL,
                text TEXT,
                image_path TEXT NOT NULL
                )
             """)

    def add_verse(self, reference, text):
        with self.get_connection() as conn:
            conn.execute(
                """
            INSERT INTO verses (reference, text)
            VALUES (?, ?)
        """,
                (reference, text),
            )

    def add_image(self, image_path):
        with self.get_connection() as conn:
            conn.execute(
                """
            INSERT INTO verses (image_path)
            VALUES (?,)
        """,
                (image_path),
            )


print("OK!")
