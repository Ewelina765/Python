import json
import os
from datetime import datetime, date

NEWS_FEED_FILE = "news_feed.txt"

def publish_news(text, city):
    publish_date = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"News -------------------------\n{text}\nCity: {city}\nDate: {publish_date}\n\n"

def publish_priv_ad(text, expiration_date):
    today = date.today()
    days_left = (expiration_date - today).days
    if days_left < 0:
        days_left = 0
    return f"Private Ad -------------------\n{text}\nExpires on: {expiration_date} ({days_left} days left)\n\n"

def publish_event(event_name, city, event_date):
    today = date.today()
    days_until = (event_date - today).days
    if days_until < 0:
        status = "Event has passed"
    elif days_until == 0:
        status = "Event is today"
    else:
        status = f"{days_until} days until event"
    return f"Event -----------------------\nEvent: {event_name}\nCity: {city}\nDate: {event_date}\nStatus: {status}\n\n"

def save_record(record):
    with open(NEWS_FEED_FILE, "a", encoding="utf-8") as f:
        f.write(record)

class JsonRecordProcessor:
    def __init__(self, input_file=None):
        self.input_file = input_file or "input_records.json"

    def process_json_file(self):
        if not os.path.isfile(self.input_file):
            print(f"File '{self.input_file}' not found.")
            return False
        with open(self.input_file, "r", encoding="utf-8") as f:
            records = json.load(f)
        for key, rec in records.items():
            pub_type = rec.get("publication_type", "").lower()
            if pub_type == "news":
                text = rec.get("text", "")
                city = rec.get("city", "")
                record = publish_news(text, city)
            elif pub_type == "ads":
                text = rec.get("text", "")
                exp_str = rec.get("date", "")
                try:
                    expiration_date = datetime.strptime(exp_str, "%Y-%m-%d").date()
                    record = publish_priv_ad(text, expiration_date)
                except ValueError:
                    print(f"Invalid date for ads: {exp_str}")
                    continue
            elif pub_type == "event":
                event_name = rec.get("text", "")
                city = rec.get("city", "")
                date_str = rec.get("date", "")
                try:
                    event_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                    record = publish_event(event_name, city, event_date)
                except ValueError:
                    print(f"Invalid event date: {date_str}")
                    continue
            else:
                print(f"Unknown publication type: {pub_type}. Skipping.")
                continue
            save_record(record)
        os.remove(self.input_file)
        print(f"Processed and removed file: {self.input_file}")
        return True

if __name__ == "__main__":
    processor = JsonRecordProcessor()
    processor.process_json_file()
