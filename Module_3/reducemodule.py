import math
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def gcd_simulation(x, y):
    print("\nStep 2: Find GCD")

    while y != 0:
        q = x // y
        r = x % y
        print(f"{x} ÷ {y} = {q} remainder {r}")
        x = y
        y = r

    print(f"gcd = {x}")
    return x

def find_common_factor(left, right):
    return math.gcd(left, right)

def reduced_modulo():
    clear_screen()

    print("===================================")
    print("      REDUCED MODULO PROGRAM")
    print("===================================")

    left = int(input("Enter left number: "))
    right = int(input("Enter right number: "))
    m = int(input("Enter modulo m: "))

    print("\nGiven:")
    print(f"{left} ≡ {right} (mod {m})")

    print("\nStep 1: Factor common number")

    c = find_common_factor(left, right)
    a = left // c
    b = right // c

    print(f"Common factor = {c}")
    print(f"{left} = {c}({a})")
    print(f"{right} = {c}({b})")

    print("\nSo:")
    print(f"{c}({a}) ≡ {c}({b}) (mod {m})")

    n = gcd_simulation(c, m)

    print("\nStep 3: Reduce modulo")
    new_mod = m // n
    print(f"{m} ÷ {n} = {new_mod}")

    print(f"\nCancel {c}:")
    print(f"{a} ≡ {b} (mod {new_mod})")

    print("\nStep 4: Check")
    difference = a - b
    print(f"{a} - {b} = {difference}")

    if difference % new_mod == 0:
        print(f"{difference} ÷ {new_mod} = {difference // new_mod}")
        print("\nTRUE.")
    else:
        print(f"{difference} is not divisible by {new_mod}")
        print("\nFALSE.")

while True:
    reduced_modulo()

    again = input("\nTry again? (yes/no): ").lower()
    if again != "yes":
        break