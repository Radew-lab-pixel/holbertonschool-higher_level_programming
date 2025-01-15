#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number < 0:
    modulus = (-1 * number) % 10
    modulus = -1 * modulus
else:
    modulus = number % 10

print(f"Last digit of {number} is {modulus} ", end="")
if modulus > 5:
    print(f"and is greater than 5")

elif modulus == 0:
    print(f"and is 0")

elif modulus < 6 and modulus != 0:
    print(f"and is less than 6 and not 0")

else:
    print(f"Error")
