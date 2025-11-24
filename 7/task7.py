import csv
import string

def process_output_file(output_file):
    with open(output_file, "r", encoding="utf-8") as f:
        text = f.read()
    # Preprocess: lowercasing, treat whole sentence as a word
    words = [w.lower() for w in text.split()]
    letters = [ch for ch in text if ch.isalpha()]
    upper_letters = [ch for ch in text if ch.isupper()]
    
    # --- WORD COUNT CSV ---
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    with open("word_count.csv", "w", newline="", encoding="utf-8") as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(["word", "count"])
        for word, count in word_counts.items():
            writer.writerow([word, count])

    # --- LETTER COUNT CSV ---
    letter_stats = {}
    total_letters = len(letters)
    for letter in string.ascii_letters:
        count_all = text.count(letter)
        count_upper = text.count(letter.upper())
        if count_all > 0:
            percent = round(count_upper / count_all * 100, 2)
        else:
            percent = 0
        letter_stats[letter.lower()] = (count_all, count_upper, percent)

    with open("letter_count.csv", "w", newline="", encoding="utf-8") as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(["letter", "count_all", "count_uppercase", "percentage"])
        for letter in string.ascii_lowercase:
            count_all, count_upper, percent = letter_stats.get(letter, (0,0,0))
            writer.writerow([letter, count_all, count_upper, percent])

process_output_file("news_feed.txt")
