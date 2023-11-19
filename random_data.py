import random

def sorted_random_numbers(length):
    random_list = [random.randint(1, 1000) for _ in range(length)]  # Generating random numbers between 1 and 1000
    random_list.sort()  # Sorting the generated random numbers
    return random_list

# Example usage: generating 10 sorted random numbers
result = sorted_random_numbers(100)
print("Sorted Random Numbers:", result)
