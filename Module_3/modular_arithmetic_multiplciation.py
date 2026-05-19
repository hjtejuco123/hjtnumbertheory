# Modular Arithmetic: Multiplication

print("==========================================")
print("   MODULAR ARITHMETIC (MULTIPLICATION)")
print("==========================================")

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

print("\nFormula ")
print("If:")
print("a ≡ b (mod n)")
print("and")
print("c ≡ d (mod n)")
print("then:")
print("ac ≡ bd (mod n)")

print("\nStep 1: Given")
print(f"{a} ≡ {b} (mod {n})")
print(f"{c} ≡ {d} (mod {n})")

print("\nStep 2: Multiply")
print(f"({a})({c}) ≡ ({b})({d}) (mod {n})")

left_side = a * c
right_side = b * d

print(f"{left_side} ≡ {right_side} (mod {n})")

print("\nStep 3: Check")
difference = left_side - right_side

print(f"{left_side} - {right_side} = {difference}")

quotient = difference // n
remainder = difference % n

print(f"{difference} ÷ {n} = {quotient} remainder {remainder}")

print("\nStep 4: Least Residue Check")
left_residue = left_side % n
right_residue = right_side % n

print(f"{left_side} mod {n} = {left_residue}")
print(f"{right_side} mod {n} = {right_residue}")

if remainder == 0:
    print("\nTRUE.")
    print("Multiplication preserves congruence.")
else:
    print("\nFALSE.")
    print("Multiplication does not preserve congruence.")

print("\nFinal Answer")
print(f"{left_side} ≡ {right_side} (mod {n})")