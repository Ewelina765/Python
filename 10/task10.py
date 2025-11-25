import sqlite3
from datetime import datetime

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''
      CREATE TABLE IF NOT EXISTS news (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          text TEXT UNIQUE,
          city TEXT,
          created_at DATETIME DEFAULT CURRENT_TIMESTAMP
      )
    ''')
    cursor.execute('''
      CREATE TABLE IF NOT EXISTS ads (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          text TEXT UNIQUE,
          expiration DATE
      )
    ''')
    cursor.execute('''
      CREATE TABLE IF NOT EXISTS event (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          text TEXT UNIQUE,
          city TEXT,
          event_date DATE
      )
    ''')
    conn.commit()

class DatabaseRecordSaver:
    def __init__(self, db_path="records.db"):
        self.conn = sqlite3.connect(db_path)
        create_tables(self.conn)

    def save_news(self, text, city):
        try:
            self.conn.execute(
                "INSERT OR IGNORE INTO news (text, city) VALUES (?, ?)", (text, city)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Error saving news: {e}")

    def save_ad(self, text, expiration):
        try:
            self.conn.execute(
                "INSERT OR IGNORE INTO ads (text, expiration) VALUES (?, ?)", (text, expiration)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Error saving ad: {e}")

    def save_event(self, text, city, event_date):
        try:
            self.conn.execute(
                "INSERT OR IGNORE INTO event (text, city, event_date) VALUES (?, ?, ?)", (text, city, event_date)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Error saving event: {e}")
    
    def select_all(self, table_name):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            print(f"Records from table '{table_name}':")
            for row in rows:
                print(row)
        except Exception as e:
            print(f"Error selecting from table {table_name}: {e}")

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    db_rec = DatabaseRecordSaver()

    # examples
    db_rec.save_news("Breaking news from Warsaw.", "Warsaw")
    db_rec.save_news("Breaking news from Warsaw.", "Warsaw")  # duplicate
    db_rec.save_ad("Sale! Up to 50% off.", "2025-12-31")
    db_rec.save_event("Python Conference", "Krakow", "2025-12-15")
    db_rec.save_event("Python Conference", "Krakow", "2025-12-15")  # duplicate

    db_rec.select_all("news")
    db_rec.select_all("ads")
    db_rec.select_all("event")

    db_rec.close()
