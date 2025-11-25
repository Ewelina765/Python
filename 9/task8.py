import os
import xml.etree.ElementTree as ET
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

class XmlRecordProcessor:
    def __init__(self, input_file=None):
        self.input_file = input_file or "input_records.xml"

    def process_xml_file(self):
        if not os.path.isfile(self.input_file):
            print(f"File '{self.input_file}' not found.")
            return False
        tree = ET.parse(self.input_file)
        root = tree.getroot()
        for rec in root.findall("record"):
            rec_type = rec.attrib.get("type", "").lower()
            if rec_type == "news":
                text = rec.findtext("text", "")
                city = rec.findtext("city", "")
                record = publish_news(text, city)
            elif rec_type == "ads":
                text = rec.findtext("text", "")
                date_str = rec.findtext("date", "")
                try:
                    expiration_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                    record = publish_priv_ad(text, expiration_date)
                except Exception:
                    print(f"Invalid date for ads: {date_str}")
                    continue
            elif rec_type == "event":
                event_name = rec.findtext("text", "")
                city = rec.findtext("city", "")
                date_str = rec.findtext("date", "")
                try:
                    event_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                    record = publish_event(event_name, city, event_date)
                except Exception:
                    print(f"Invalid event date: {date_str}")
                    continue
            else:
                print(f"Unknown record type: {rec_type}. Skipping.")
                continue
            save_record(record)
        os.remove(self.input_file)
        print(f"Processed and removed file: {self.input_file}")
        return True

if __name__ == "__main__":
    processor = XmlRecordProcessor()
    processor.process_xml_file()
