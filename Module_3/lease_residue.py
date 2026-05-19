# Least Residue Program with Detailed Simulation

print("===================================")
print("   LEAST RESIDUE PROGRAM")
print("===================================")

# User input
a = int(input("Enter the number a: "))
m = int(input("Enter the modulo m: "))

print("\nGiven:")
print(f"{a} (mod {m})")

# Compute quotient and remainder
quotient = a // m
remainder = a % m

print("\nStep 1: Divide")
print(f"{a} ÷ {m} = {quotient} remainder {remainder}")

print("\nStep 2: Write in division form")
print(f"{a} = {quotient}({m}) + {remainder}")

print("\nStep 3: Congruence form")
print(f"{a} ≡ {remainder} (mod {m})")

print("\nAnswer:")
print(f"Least residue: {remainder}")

# Step 4 Detailed Simulation
print("\nStep 4: Possible least residues")
print(f"For modulo {m}, the least residues are:\n")

for i in range(m):
    print(f"Remainder {i}")

print("\nExplanation:")
print(f"When dividing by {m},")
print(f"the remainder must always be from 0 up to {m-1}.")

print("\nSimulation using division:")

for i in range(m):
    sample = m + i
    q = sample // m
    r = sample % m

    print(f"{sample} ÷ {m} = {q} remainder {r}")

print("\nTherefore, the only possible least residues are:")

for i in range(m):
    print(i, end=" ")

print()

# Step 5 Detailed Verification
print("\nStep 5: Verification")

difference = a - remainder

print(f"Subtract the least residue from the original number:")
print(f"{a} - {remainder} = {difference}")

print("\nNow divide the difference by the modulo:")

verify_q = difference // m
verify_r = difference % m

print(f"{difference} ÷ {m} = {verify_q} remainder {verify_r}")

if verify_r == 0:
    print("\nSince the remainder is 0,")
    print(f"{difference} is divisible by {m}.")
    print("TRUE: They are congruent.")
else:
    print("\nSince the remainder is not 0,")
    print(f"{difference} is NOT divisible by {m}.")
    print("FALSE: They are not congruent.")

print("\nFinal Answer:")
print(f"{a} ≡ {remainder} (mod {m})")