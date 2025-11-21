import re

# Original text assigned to a variable
text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# 1. Fix the word 'iZ' only when it's a mistaken word (case insensitive, whole word)
text = re.sub(r'\biZ\b', 'is', text, flags=re.IGNORECASE)

# 2. Normalize the text to lowercase
normalized_text = text.lower()

# 3. Create a new sentence composed of the last words of each existing sentence

# Split the text into sentences by period followed by optional spaces/newlines
sentences = re.split(r'\.\s*', normalized_text.strip())
sentences = [s for s in sentences if s]  # Remove empty strings

# Extract the last word from each sentence
last_words = [s.split()[-1] for s in sentences if s.split()]

# Create the new sentence by joining last words and adding a period
new_sentence = " ".join(last_words) + "."

# Append the new sentence to the normalized text
final_text = normalized_text + "\n\n" + new_sentence

# 4. Count all whitespace characters (spaces, tabs, newlines, etc.)
whitespace_count = len(re.findall(r' ', final_text))

# Print results
print("Normalized and corrected text:\n")
print(final_text)
print(f"\nNumber of whitespace characters in the text: {whitespace_count}")
