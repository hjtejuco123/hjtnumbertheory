# Congruence Using Remainders

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
m = int(input("Enter modulus: "))

# Step 1: Find remainders
r1 = a % m
r2 = b % m

print("\nStep 1: Divide", a, "by", m)
print(a, "÷", m, "=", a // m, "remainder", r1)

print("\nStep 2: Divide", b, "by", m)
print(b, "÷", m, "=", b // m, "remainder", r2)

print("\nStep 3: Compare the remainders")

if r1 == r2:
    print("Both have remainder", r1)
    print("\nSo:")
    print(a, "≡", b, "(mod", m, ")")
    print("TRUE")
else:
    print("The remainders are different.")
    print("\nSo:")
    print(a, "≢", b, "(mod", m, ")")
    print("FALSE")