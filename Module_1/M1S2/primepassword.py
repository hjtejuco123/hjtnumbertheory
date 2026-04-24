#Enter the name
#Enter a number 

import random

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

name = input("Enter your name: ")
number = int(input("Enter a number: "))

p = random.choice(primes) #pick random prime number from the list

password = f"{name}_{number *p}"

print ("\n Generated Password:", password)