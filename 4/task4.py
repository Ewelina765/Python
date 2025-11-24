import random
import string
import re
 # Refactor homeworks from module 2 and 3 using functional approach with decomposition.
# Homework 2 functions

def generate_random_dicts(min_dicts=2, max_dicts=10, min_keys=2, max_keys=10):
    dict_list = []
    n_dicts = random.randint(min_dicts, max_dicts)
    for _ in range(n_dicts):
        n_keys = random.randint(min_keys, max_keys)
        keys = random.sample(string.ascii_lowercase, n_keys)
        d = {k: random.randint(0,100) for k in keys}
        dict_list.append(d)
    return dict_list

def merge_dicts_with_rules(dict_list):
    key_info = {}
    # Track max value and source dict index for keys in multiple dicts
    for idx, d in enumerate(dict_list, 1):   # dict numbered from 1
        for k, v in d.items():
            if k not in key_info or v > key_info[k][0]:
                key_info[k] = (v, idx)
    # Count how many dicts each key appeared in
    key_counts = {}
    for d in dict_list:
        for k in d:
            key_counts[k] = key_counts.get(k, 0) + 1
    # Create merged result with keys renamed if multiple occurrences
    result = {}
    for k in key_info:
        v, idx = key_info[k]
        if key_counts[k] > 1:
            result[f"{k}_{idx}"] = v
        else:
            result[k] = v
    return result

def homework_2():
    dicts = generate_random_dicts()
    print("Generated dicts:")
    print(dicts)
    merged = merge_dicts_with_rules(dicts)
    print("Merged result dict:")
    print(merged)


# Homework 3 functions

def fix_iz_words(text):
    # Fix 'iZ' only when mistaken word (whole word, case insensitive)
    return re.sub(r'\biZ\b', 'is', text, flags=re.IGNORECASE)

def normalize_text(text):
    return text.lower()

def extract_sentences(text):
    sentences = re.split(r'\.\s*', text.strip())
    return [s for s in sentences if s]

def build_sentence_from_last_words(sentences):
    last_words = [s.split()[-1] for s in sentences if s.split()]
    return " ".join(last_words) + "."

def count_whitespaces(text):
    # Count all whitespace characters including tabs, newlines, spaces
    return len(re.findall(r'\s', text))

def homework_3():
    original_text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.


  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.


  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.


  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

    fixed_text = fix_iz_words(original_text)
    normalized = normalize_text(fixed_text)
    sentences = extract_sentences(normalized)
    new_sentence = build_sentence_from_last_words(sentences)
    final_text = normalized + "\n\n" + new_sentence
    whitespace_count = count_whitespaces(final_text)

    print("Normalized and corrected text:\n")
    print(final_text)
    print(f"\nNumber of whitespace characters in the text: {whitespace_count}")

# Run the homeworks
homework_2()
homework_3()
