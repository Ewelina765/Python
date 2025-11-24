from datetime import datetime, date

# File to write published news into
NEWS_FEED_FILE = "news_feed.txt"

def input_news():
    text = input("Enter news text: ").strip()
    city = input("Enter city: ").strip()
    return text, city

def input_priv_ad():
    text = input("Enter private ad text: ").strip()
    while True:
        exp_str = input("Enter expiration date (YYYY-MM-DD): ").strip()
        try:
            expiration_date = datetime.strptime(exp_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Please enter date as YYYY-MM-DD.")
    return text, expiration_date

def input_event():
    event_name = input("Enter event name: ").strip()
    city = input("Enter city: ").strip()
    while True:
        event_date_str = input("Enter event date (YYYY-MM-DD): ").strip()
        try:
            event_date = datetime.strptime(event_date_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Please enter date as YYYY-MM-DD.")
    return event_name, city, event_date

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

def main():
    print("Select type of record to add:")
    print("1 - News")
    print("2 - Private Ad")
    print("3 - Event (unique)")
    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        text, city = input_news()
        record = publish_news(text, city)
    elif choice == "2":
        text, expiration_date = input_priv_ad()
        record = publish_priv_ad(text, expiration_date)
    elif choice == "3":
        event_name, city, event_date = input_event()
        record = publish_event(event_name, city, event_date)
    else:
        print("Invalid choice!")
        return

    save_record(record)
    print("Record added successfully to", NEWS_FEED_FILE)
    print("Please commit the file in git for review.")

if __name__ == "__main__":
    main()
