

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

# Check the original congruences first
print("\n================ CHECK GIVEN CONGRUENCES =================")

a_residue = a % n
b_residue = b % n
c_residue = c % n
d_residue = d % n

print(f"{a} mod {n} = {a_residue}")
print(f"{b} mod {n} = {b_residue}")

if a_residue == b_residue:
    print(f"So, {a} ≡ {b} (mod {n}) is TRUE.")
else:
    print(f"So, {a} ≡ {b} (mod {n}) is FALSE.")

print()

print(f"{c} mod {n} = {c_residue}")
print(f"{d} mod {n} = {d_residue}")

if c_residue == d_residue:
    print(f"So, {c} ≡ {d} (mod {n}) is TRUE.")
else:
    print(f"So, {c} ≡ {d} (mod {n}) is FALSE.")

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

    left_side = a + c
    right_side = b + d

    print("\nStep 2: Add both sides")
    print(f"{a} + {c} ≡ {b} + {d} (mod {n})")
    print(f"{left_side} ≡ {right_side} (mod {n})")

    print("\nStep 3: Check if the difference is divisible by n")

    difference = left_side - right_side
    quotient = difference // n
    remainder = difference % n

    print(f"{left_side} - {right_side} = {difference}")
    print(f"{difference} ÷ {n} = {quotient} remainder {remainder}")

    if remainder == 0:
        print(f"Because the remainder is 0, {difference} is divisible by {n}.")
    else:
        print(f"Because the remainder is not 0, {difference} is not divisible by {n}.")

    print("\nStep 4: Least Residues")

    left_residue = left_side % n
    right_residue = right_side % n

    print(f"{left_side} mod {n} = {left_residue}")
    print(f"{right_side} mod {n} = {right_residue}")

    print("\nSo:")
    print(f"{left_side} ≡ {left_residue} (mod {n})")
    print(f"{right_side} ≡ {right_residue} (mod {n})")

    print("\nFinal Conclusion")

    if left_residue == right_residue:
        print("TRUE.")
        print(f"{left_side} ≡ {right_side} (mod {n})")
        print("Addition preserves congruence.")
    else:
        print("FALSE.")
        print("Addition does not preserve congruence because the given values are not congruent.")

# ==================================================
# SUBTRACTION
# ==================================================
elif choice == 2:

    print("\n================ SUBTRACTION =================")

    print("\nStep 1: Given")
    print(f"{a} ≡ {b} (mod {n})")
    print(f"{c} ≡ {d} (mod {n})")

    left_side = a - c
    right_side = b - d

    print("\nStep 2: Subtract both sides")
    print(f"{a} - {c} ≡ {b} - {d} (mod {n})")
    print(f"{left_side} ≡ {right_side} (mod {n})")

    print("\nStep 3: Check if the difference is divisible by n")

    difference = left_side - right_side
    quotient = difference // n
    remainder = difference % n

    print(f"{left_side} - ({right_side}) = {difference}")
    print(f"{difference} ÷ {n} = {quotient} remainder {remainder}")

    if remainder == 0:
        print(f"Because the remainder is 0, {difference} is divisible by {n}.")
    else:
        print(f"Because the remainder is not 0, {difference} is not divisible by {n}.")

    print("\nStep 4: Least Residues")

    left_residue = left_side % n
    right_residue = right_side % n

    print(f"{left_side} mod {n} = {left_residue}")
    print(f"{right_side} mod {n} = {right_residue}")

    print("\nSo:")
    print(f"{left_side} ≡ {left_residue} (mod {n})")
    print(f"{right_side} ≡ {right_residue} (mod {n})")

    print("\nFinal Conclusion")

    if left_residue == right_residue:
        print("TRUE.")
        print(f"{left_side} ≡ {right_side} (mod {n})")
        print("Subtraction preserves congruence.")
    else:
        print("FALSE.")
        print("Subtraction does not preserve congruence because the given values are not congruent.")

else:
    print("Invalid choice.")