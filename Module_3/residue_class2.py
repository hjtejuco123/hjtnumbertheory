import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def residue_class():
    clear_screen()

    print("===================================")
    print("        RESIDUE CLASS PROGRAM")
    print("===================================")

    # USER INPUT
    a = int(input("Enter residue number a: "))
    m = int(input("Enter modulo m: "))

    # VALIDATION
    if m <= 0:
        print("\nModulo must be a positive integer.")
        return

    print("\nGiven:")
    print(f"{a} (mod {m})")

    # EXPLANATION
    print("\nExplanation:")
    print(f"We need to find all integers x such that:")
    print(f"x ≡ {a} (mod {m})")

    print("\nDefinition of Congruence:")
    print(f"x ≡ {a} (mod {m})  iff  {m} divides (x - {a})")

    print("\nMeaning:")
    print(f"All numbers in this residue class leave remainder {a % m}")
    print(f"when divided by {m}.")

    # STEP 1
    print("\n===================================")
    print("Step 1: Generate the Residue Class")
    print("===================================")

    print("\nFormula:")
    print(f"x = {a} + {m}k")
    print("where k is any integer")

    numbers = []

    for k in range(-5, 6):
        value = a + (m * k)
        numbers.append(value)

    print("\nResidue Class:")
    print("..., ", end="")

    for i in range(len(numbers)):
        if i != len(numbers) - 1:
            print(numbers[i], end=", ")
        else:
            print(numbers[i], end="")

    print(", ...")

    # STEP 2
    print("\n===================================")
    print("Step 2: Verify Using Division")
    print("===================================")

    for num in numbers:

        quotient = num // m
        remainder = num % m

        print(f"\n{num} ÷ {m} = {quotient} remainder {remainder}")

        if remainder == a % m:
            print(f"So, {num} ≡ {a} (mod {m})")

    # STEP 3
    print("\n===================================")
    print("Step 3: Check Using Difference")
    print("===================================")

    positive_numbers = [x for x in numbers if x >= a]

    for num in positive_numbers[:4]:

        difference = num - a

        print(f"\n{num} - {a} = {difference}")

        if difference % m == 0:
            print(f"{difference} is divisible by {m}")
            print(f"So, {num} ≡ {a} (mod {m})")

    # STEP 4
    print("\n===================================")
    print("Step 4: Final Congruence Form")
    print("===================================")

    for i in range(min(4, len(positive_numbers))):

        print(positive_numbers[i], end="")

        if i != min(4, len(positive_numbers)) - 1:
            print(" ≡ ", end="")

    print(f" (mod {m})")

    # FINAL ANSWER
    print("\n===================================")
    print("Final Answer")
    print("===================================")

    print(f"\n[{a}] = {{ x | x ≡ {a} (mod {m}) }}")

    print("\nGeneral Formula:")
    print(f"[{a}] = {{ {a} + {m}k | k ∈ Z }}")

    print("\nImportant Notes:")
    print(f"• Numbers in the same residue class differ by multiples of {m}")
    print(f"• Adding or subtracting {m} does not change the remainder")
    print(f"• Modulo {m} has residue classes:")
    
    for i in range(m):
        print(f"  [{i}]", end=" ")

    print()


def main():

    while True:

        residue_class()

        again = input("\nDo you want to try again? (yes/no): ").lower()

        if again != "yes":
            print("\nProgram ended.")
            break


main()