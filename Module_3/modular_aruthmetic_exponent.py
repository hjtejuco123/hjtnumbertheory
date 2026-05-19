# Modular Exponentiation Program

print("===================================")
print("      MODULAR EXPONENTIATION")
print("===================================")

# Required Variables
a = int(input("Enter original base a: "))
m = int(input("Enter exponent m: "))
n = int(input("Enter modulo n: "))

# Compute least residue of a
b = a % n

print("\nRequired Variables")
print(f"a = {a}")
print(f"b = {b}  <-- least residue of a")
print(f"m = {m}")
print(f"n = {n}")

print("\nFormula")
print("If:")
print("a ≡ b (mod n)")
print("then:")
print("a^m ≡ b^m (mod n)")

print("\nFind:")
print(f"{a}^{m} (mod {n})")

print("\nStep 1: Reduce the base")
print(f"{a} ÷ {n} = {a // n} remainder {b}")
print(f"So: {a} ≡ {b} (mod {n})")

print("\nStep 2: Apply power rule")
print(f"{a}^{m} ≡ {b}^{m} (mod {n})")

print("\nStep 3: Compute the smaller power")
power_value = b ** m
print(f"{b}^{m} = {power_value}")

print("\nStep 4: Divide by modulo")
quotient = power_value // n
remainder = power_value % n

print(f"{power_value} ÷ {n} = {quotient} remainder {remainder}")

print("\nAnswer")
print(f"{a}^{m} ≡ {remainder} (mod {n})")
print(f"Least residue: {remainder}")

print("\nVerification using direct computation")
direct_value = a ** m
direct_remainder = direct_value % n

print(f"{a}^{m} = {direct_value}")
print(f"{direct_value} mod {n} = {direct_remainder}")

if direct_remainder == remainder:
    print("TRUE.")
else:
    print("FALSE.")