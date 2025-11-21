# Write a code, which will:

# 1. create a list of random number of dicts (from 2 to 10)

# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
# 2. get previously generated list of dicts and create one common dict:

# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

import random
import string

# 1. Generate a list of random dicts (from 2 to 10)
dict_list = []
n_dicts = random.randint(2, 10)

for i in range(n_dicts):
    n_keys = random.randint(2, 10)
    keys = random.sample(string.ascii_lowercase, n_keys)
    d = {k: random.randint(0,100) for k in keys}
    dict_list.append(d)

print("Generated dicts:")
print(dict_list)

# 2. Merge dicts with the described rules
result = {}

# Keep max value and track source dict index for keys seen in multiple dicts
key_info = {}

for idx, d in enumerate(dict_list, 1):    # dict numbered from 1
    for k, v in d.items():
        if k not in key_info or v > key_info[k][0]:
            key_info[k] = (v, idx)

# Count how many dicts each key appeared in
key_counts = {}
for d in dict_list:
    for k in d:
        key_counts[k] = key_counts.get(k, 0) + 1

for k in key_info:
    v, idx = key_info[k]
    if key_counts[k] > 1:
        result[f"{k}_{idx}"] = v
    else:
        result[k] = v

print("Merged result dict:")
print(result)



