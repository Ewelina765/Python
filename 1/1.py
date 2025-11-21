# Create a python script:
# create list of 100 random numbers from 0 to 1000
# sort list from min to max (without using sort())
# calculate average for even and odd numbers
# print both average result in console 

import random  # Import random module to generate random numbers

# Create a list of 100 random integers between 0 and 1000
numbers = [random.randint(0, 1000) for _ in range(100)]

# Function to sort a list using bubble sort (without using sort())
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Swap adjacent elements if they are in wrong order
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

# Sort the 'numbers' list from min to max
bubble_sort(numbers)

# Separate even and odd numbers into different lists
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# Calculate average for even numbers, check to avoid division by zero
average_even = sum(even_numbers) / len(even_numbers) if even_numbers else 0

# Calculate average for odd numbers, check to avoid division by zero
average_odd = sum(odd_numbers) / len(odd_numbers) if odd_numbers else 0

# Print both average results to the console
print(f"Average of even numbers: {average_even}")
print(f"Average of odd numbers: {average_odd}")
