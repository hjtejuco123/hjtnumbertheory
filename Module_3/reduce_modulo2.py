import math
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def gcd_simulation(x, y):
    print("\nStep 2: Find GCD")
    print(f"\nWe find:\n")
    print(f"gcd({x},{y})")
    print("\nUsing division:\n")

    original_x = x
    original_y = y

    while y != 0:
        q = x // y
        r = x % y
        print(f"{x} ÷ {y} = {q} remainder {r}")
        x = y
        y = r

    print(f"\nSo:\n")
    print(f"gcd({original_x},{original_y}) = {x}")
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

    print("\nGiven:\n")
    print(f"{left} ≡ {right} (mod {m})")

    print("\nThis means:\n")
    difference_original = left - right
    print(f"{left} - {right} = {difference_original}")

    if difference_original % m == 0:
        print(f"\nSince {difference_original} is divisible by {m}, the congruence is true.")
    else:
        print(f"\nSince {difference_original} is not divisible by {m}, the congruence is false.")

    print("\nStep 1: Factor common number\n")

    c = find_common_factor(left, right)
    a = left // c
    b = right // c

    print(f"Both {left} and {right} have a common factor of {c}.\n")
    print(f"{left} = {c}({a})")
    print(f"{right} = {c}({b})")

    print("\nSo:\n")
    print(f"{c}({a}) ≡ {c}({b}) (mod {m})")

    n = gcd_simulation(c, m)

    print("\nStep 3: Reduce the modulo\n")
    print("Divide the modulo by the GCD:\n")

    new_mod = m // n
    print(f"{m} ÷ {n} = {new_mod}")

    print(f"\nNow cancel the common factor {c}:\n")
    print(f"{a} ≡ {b} (mod {new_mod})")

    print("\nStep 4: Check\n")
    print("Subtract:\n")

    reduced_difference = a - b
    print(f"{a} - {b} = {reduced_difference}")

    print(f"\nCheck if {reduced_difference} is divisible by {new_mod}:\n")

    if reduced_difference % new_mod == 0:
        print(f"{reduced_difference} ÷ {new_mod} = {reduced_difference // new_mod}")
        print("\nNo remainder, so it is true.")

        print("\nFinal Answer")
        print(f"{left} ≡ {right} (mod {m})")
        print("\ncan be reduced to:\n")
        print(f"{a} ≡ {b} (mod {new_mod})")
        print("\nTherefore:\n")
        print("TRUE.")
    else:
        print(f"{reduced_difference} is not divisible by {new_mod}")
        print("\nTherefore:\n")
        print("FALSE.")

while True:
    reduced_modulo()

    again = input("\nTry again? (yes/no): ").lower()
    if again != "yes":
        break