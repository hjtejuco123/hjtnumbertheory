# Modular Arithmetic (Addition and Subtraction)
# Based on Congruence Property from the Slide

print("====================================================")
print(" MODULAR ARITHMETIC (ADDITION AND SUBTRACTION)")
print("====================================================")

# Required Variables
a = int(input("Enter first congruent number a: "))
b = int(input("Enter second congruent number b: "))
c = int(input("Enter third number c: "))
d = int(input("Enter fourth number d: "))
n = int(input("Enter modulo n: "))

print("\nRequired Variables")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"d = {d}")
print(f"n = {n}")

print("\nFormula from the Slide")

print("If:")
print("a ≡ b (mod n)")
print("and")
print("c ≡ d (mod n)")

print("\nthen:")
print("a + c ≡ b + d (mod n)")
print("a - c ≡ b - d (mod n)")

print("\nAddition or subtraction preserves congruence.")

print("\nChoose Operation")
print("1. Addition")
print("2. Subtraction")

choice = int(input("Enter choice: "))

# ==================================================
# ADDITION
# ==================================================
if choice == 1:

    print("\n================ ADDITION =================")

    print("\nStep 1: Given")
    print(f"{a} ≡ {b} (mod {n})")
    print(f"{c} ≡ {d} (mod {n})")

    # Perform addition
    left_side = a + c
    right_side = b + d

    print("\nStep 2: Add both sides")
    print(f"{a} + {c} ≡ {b} + {d} (mod {n})")

    print(f"{left_side} ≡ {right_side} (mod {n})")

    # Verification
    print("\nStep 3: Check")

    difference = left_side - right_side

    print(f"{left_side} - {right_side} = {difference}")

    quotient = difference // n
    remainder = difference % n

    print(f"{difference} ÷ {n} = {quotient} remainder {remainder}")

    # Least residues
    left_residue = left_side % n
    right_residue = right_side % n

    print("\nStep 4: Least Residues")

    print(f"{left_side} mod {n} = {left_residue}")
    print(f"{right_side} mod {n} = {right_residue}")

    print(f"\nSo:")
    print(f"{left_side} ≡ {left_residue} (mod {n})")
    print(f"{right_side} ≡ {right_residue} (mod {n})")

    if remainder == 0:
        print("\nTRUE.")
        print("Addition preserves congruence.")
    else:
        print("\nFALSE.")

# ==================================================
# SUBTRACTION
# ==================================================
elif choice == 2:

    print("\n================ SUBTRACTION =================")

    print("\nStep 1: Given")
    print(f"{a} ≡ {b} (mod {n})")
    print(f"{c} ≡ {d} (mod {n})")

    # Perform subtraction
    left_side = a - c
    right_side = b - d

    print("\nStep 2: Subtract both sides")
    print(f"{a} - {c} ≡ {b} - {d} (mod {n})")

    print(f"{left_side} ≡ {right_side} (mod {n})")

    # Verification
    print("\nStep 3: Check")

    difference = left_side - right_side

    print(f"{left_side} - {right_side} = {difference}")

    quotient = difference // n
    remainder = difference % n

    print(f"{difference} ÷ {n} = {quotient} remainder {remainder}")

    # Least residues
    left_residue = left_side % n
    right_residue = right_side % n

    print("\nStep 4: Least Residues")

    print(f"{left_side} mod {n} = {left_residue}")
    print(f"{right_side} mod {n} = {right_residue}")

    print(f"\nSo:")
    print(f"{left_side} ≡ {left_residue} (mod {n})")
    print(f"{right_side} ≡ {right_residue} (mod {n})")

    if remainder == 0:
        print("\nTRUE.")
        print("Subtraction preserves congruence.")
    else:
        print("\nFALSE.")

else:
    print("Invalid choice.")