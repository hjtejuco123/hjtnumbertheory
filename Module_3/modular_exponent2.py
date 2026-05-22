# Modular Exponentiation Program
# with Least Residue Computation

import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()

print("===================================")
print("    MODULAR EXPONENTIATION")
print("===================================")

# Required Variables
a = int(input("Enter original base a: "))
m = int(input("Enter exponent m: "))
n = int(input("Enter modulo n: "))

# Compute least residue of a
b = a % n

print("\n===================================")
print("        REQUIRED VARIABLES")
print("===================================")

print(f"a = {a}")
print(f"b = {b}  <-- least residue of a")
print(f"m = {m}")
print(f"n = {n}")

print("\n===================================")
print("              FORMULA")
print("===================================")

print("If:")
print("a ≡ b (mod n)")
print("then:")
print("a^m ≡ b^m (mod n)")

print("\n===================================")
print("               GIVEN")
print("===================================")

print(f"Find:")
print(f"{a}^{m} (mod {n})")

print("\n===================================")
print("     STEP 1: COMPUTE LEAST RESIDUE")
print("===================================")

quotient1 = a // n
least_residue = a % n

print(f"{a} ÷ {n} = {quotient1} remainder {least_residue}")

print("\nTherefore:")
print(f"Least residue of {a} modulo {n} is {least_residue}")

print(f"\nSo:")
print(f"{a} ≡ {least_residue} (mod {n})")

print("\n===================================")
print("      STEP 2: APPLY POWER RULE")
print("===================================")

print(f"{a}^{m} ≡ {least_residue}^{m} (mod {n})")

print("\n===================================")
print("    STEP 3: COMPUTE SMALLER POWER")
print("===================================")

power_value = least_residue ** m

print(f"{least_residue}^{m} = {power_value}")

print("\n===================================")
print("      STEP 4: DIVIDE BY MODULO")
print("===================================")

quotient2 = power_value // n
remainder = power_value % n

print(f"{power_value} ÷ {n} = {quotient2} remainder {remainder}")

print("\n===================================")
print("              ANSWER")
print("===================================")

print(f"{a}^{m} ≡ {remainder} (mod {n})")

print(f"\nLeast residue:")
print(f"{remainder}")

print("\n===================================")
print("            VERIFICATION")
print("===================================")

direct_value = a ** m
direct_remainder = direct_value % n

print(f"{a}^{m} = {direct_value}")

print(f"{direct_value} ÷ {n} = {direct_value // n} remainder {direct_remainder}")

print(f"\nSo:")
print(f"{direct_value} ≡ {direct_remainder} (mod {n})")

print("\nChecking:")

if direct_remainder == remainder:
    print("TRUE.")
    print("Both methods give the same least residue.")
else:
    print("FALSE.")

print("\n===================================")
print("         END OF PROGRAM")
print("===================================")