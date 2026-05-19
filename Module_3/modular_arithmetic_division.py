# Modular Arithmetic: Division

print("====================================")
print("   MODULAR ARITHMETIC (DIVISION)")
print("====================================")

# Required Variables
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter divisor c: "))
m = int(input("Enter modulo m: "))

print("\nRequired Variables")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"m = {m}")

print("\nFormula")
print("Division preserves congruence ONLY IF:")
print("gcd(c, m) = 1")

print("\nIf:")
print("ac ≡ bc (mod m)")
print("then:")
print("a ≡ b (mod m)")
print("ONLY when gcd(c, m) = 1")

# GCD simulation
print("\nStep 1: Check GCD")
x = c
y = m

print(f"Find gcd({c}, {m})")

while y != 0:
    q = x // y
    r = x % y
    print(f"{x} ÷ {y} = {q} remainder {r}")
    x = y
    y = r

gcd_value = x
print(f"gcd({c}, {m}) = {gcd_value}")

if gcd_value == 1:
    print("\nDivision allowed.")
else:
    print("\nDivision NOT allowed.")

# Division
print("\nStep 2: Divide both numbers by c")

left = a / c
right = b / c

print(f"{a} ÷ {c} = {left}")
print(f"{b} ÷ {c} = {right}")

# Check if division gives whole numbers
if a % c == 0 and b % c == 0:
    left = a // c
    right = b // c

    print("\nStep 3: Write congruence")
    print(f"{left} ≡ {right} (mod {m})")

    print("\nStep 4: Check")
    difference = right - left

    print(f"{right} - {left} = {difference}")

    quotient = difference // m
    remainder = difference % m

    if remainder == 0:
        print(f"{difference} ÷ {m} = {quotient} remainder {remainder}")
        print("\nTRUE.")
        print(f"{left} ≡ {right} (mod {m})")
    else:
        print(f"{difference} is not divisible by {m}")
        print(f"{difference} ÷ {m} = {quotient} remainder {remainder}")
        print("\nFALSE.")
        print(f"{left} is NOT congruent to {right} (mod {m})")

else:
    print("\nCannot continue cleanly because division did not produce whole numbers.")