#Enter the name
#Enter a number 

import random

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

name = input("Enter your name: ")
number = int(input("Enter a number: "))

p1 = random.choice(primes) #pick random prime number from the list
p2 = random.choice(primes) #pick another random prime number from the list
password = f"{name}_{number * p1 * p2}"

print ("\n Generated Password:", password)