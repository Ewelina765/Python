from datetime import datetime, date
import os
import re

NEWS_FEED_FILE = "news_feed.txt"

# Normalization function inspired by Homework 3/4
def normalize_text(text):
    # Lowercase all text (can be extended with more complex normalization)
    return text.lower()

# Previous publishing and input functions omitted for brevity
# Use the same publish_news, publish_priv_ad, publish_event, save_record functions from before
# Redefining minimal helpers here

def publish_news(text, city):
    publish_date = datetime.now().strftime("%Y-%m-%d %H:%M")
    record = f"News -------------------------\n{text}\nCity: {city}\nDate: {publish_date}\n\n"
    return record

def publish_priv_ad(text, expiration_date):
    today = date.today()
    days_left = (expiration_date - today).days
    if days_left < 0:
        days_left = 0
    record = f"Private Ad -------------------\n{text}\nExpires on: {expiration_date} ({days_left} days left)\n\n"
    return record

def publish_event(event_name, city, event_date):
    today = date.today()
    days_until = (event_date - today).days
    if days_until < 0:
        status = "Event has passed"
    elif days_until == 0:
        status = "Event is today"
    else:
        status = f"{days_until} days until event"
    record = f"Event -----------------------\nEvent: {event_name}\nCity: {city}\nDate: {event_date}\nStatus: {status}\n\n"
    return record

def save_record(record):
    with open(NEWS_FEED_FILE, "a", encoding="utf-8") as f:
        f.write(record)

# File reader class

class FileRecordProcessor:
    def __init__(self, input_file=None):
        self.input_file = input_file or "input_records.txt"

    def process_file(self):
        if not os.path.isfile(self.input_file):
            print(f"File '{self.input_file}' not found.")
            return False

        with open(self.input_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Assume records are separated by ---- line, and each record starts with type line:
        # Format example:
        # Type: News
        # Text: Some text here
        # City: Moscow
        #
        # Type: PrivateAd
        # Text: Sale ends soon
        # Expiration: 2025-12-31
        #
        # Type: Event
        # EventName: Festival
        # City: Berlin
        # Date: 2025-11-30
        records = [r.strip() for r in content.split("----") if r.strip()]
        for rec in records:
            fields = {}
            for line in rec.splitlines():
                # Skip empty lines
                if not line.strip():
                    continue
                key, _, val = line.partition(":")
                fields[key.strip().lower()] = val.strip()
            # Normalize textual fields where applicable
            record_type = fields.get("type", "").lower()
            if record_type == "news":
                text = normalize_text(fields.get("text", ""))
                city = normalize_text(fields.get("city", ""))
                record = publish_news(text, city)
            elif record_type == "privatead":
                text = normalize_text(fields.get("text", ""))
                exp_str = fields.get("expiration", "")
                try:
                    expiration_date = datetime.strptime(exp_str, "%Y-%m-%d").date()
                    record = publish_priv_ad(text, expiration_date)
                except ValueError:
                    print(f"Skipping record due to invalid expiration date: {exp_str}")
                    continue
            elif record_type == "event":
                event_name = normalize_text(fields.get("eventname", ""))
                city = normalize_text(fields.get("city", ""))
                date_str = fields.get("date", "")
                try:
                    event_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                    record = publish_event(event_name, city, event_date)
                except ValueError:
                    print(f"Skipping record due to invalid event date: {date_str}")
                    continue
            else:
                print(f"Unknown record type: {record_type}. Skipping.")
                continue
            save_record(record)

        # Remove file if processed successfully
        try:
            os.remove(self.input_file)
            print(f"Processed and removed file: {self.input_file}")
        except Exception as e:
            print(f"Failed to remove file: {e}")
        return True

# Example use with file input
if __name__ == "__main__":
    processor = FileRecordProcessor()
    processor.process_file()

