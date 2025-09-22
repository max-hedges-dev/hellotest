import random

print("hello")
print("world")

# Create an array and populate it with 20 random numbers between 1 and 100
random_numbers = [random.randint(1, 100) for _ in range(20)]

# Print the array
print(random_numbers)