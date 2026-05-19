# Congruence / Residue Class Program

print("======================================")
print("   CONGRUENCE / RESIDUE CLASS PROGRAM")
print("======================================")

# User input
n = int(input("Enter modulo n: "))
r = int(input("Enter remainder/residue r: "))

print("\nGiven:")
print(f"Residue class: {r} (mod {n})")

# Check valid remainder
if r < 0 or r >= n:
    print("\nNote:")
    print(f"In modulo {n}, valid remainders are from 0 to {n - 1}.")
    r = r % n
    print(f"So your residue is reduced to: {r} (mod {n})")

print("\nStep 1: Possible remainders")
print(f"Modulo {n} has these possible remainders:")
for i in range(n):
    print(i, end=" ")
print()

print("\nStep 2: Generate numbers in the residue class")
print(f"Numbers that have remainder {r} when divided by {n}:")

numbers = []

# Generate negative and positive numbers
for k in range(-5, 6):
    value = r + (n * k)
    numbers.append(value)

print(numbers)

print("\nStep 3: Verify each number")
for num in numbers:
    quotient = num // n
    remainder = num % n

    print(f"{num} ÷ {n} = {quotient} remainder {remainder}")

print("\nStep 4: Congruence form")
positive_numbers = [num for num in numbers if num >= 0]

for i in range(len(positive_numbers)):
    print(positive_numbers[i], end="")
    if i < len(positive_numbers) - 1:
        print(" ≡ ", end="")

print(f" (mod {n})")

print("\nConclusion:")
print(f"All these numbers belong to the same residue class {r} modulo {n}.")