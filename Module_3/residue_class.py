import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def residue_class():
    clear_screen()

    print("===================================")
    print("        RESIDUE CLASS PROGRAM")
    print("===================================")

    a = int(input("Enter residue number a: "))
    m = int(input("Enter modulo m: "))

    print("\nGiven:")
    print(f"{a} (mod {m})")

    print("\nExplanation:")
    print(f"We need to find all numbers that have remainder {a} when divided by {m}.")
    print(f"These numbers belong to the residue class of {a} modulo {m}.")

    print("\nStep 1: List numbers with the same remainder")

    numbers = []

    for k in range(-5, 6):
        value = a + (m * k)
        numbers.append(value)

    print("Residue class:")
    print("..., ", end="")
    for num in numbers:
        print(num, end=", ")
    print("...")

    print("\n\nStep 2: Verify some numbers")

    for num in numbers:
        quotient = num // m
        remainder = num % m

        print(f"{num} ÷ {m} = {quotient} remainder {remainder}")

        if remainder == a % m:
            print(f"So, {num} ≡ {a} (mod {m})")
        else:
            print(f"{num} is not congruent to {a} modulo {m}")

        print()

    print("Step 3: Final Congruence Form")

    positive_numbers = [num for num in numbers if num >= a]

    for i in range(min(4, len(positive_numbers))):
        print(positive_numbers[i], end="")
        if i != min(4, len(positive_numbers)) - 1:
            print(" ≡ ", end="")

    print(f" (mod {m})")

    print("\nFinal Answer:")
    print(f"The residue class of {a} modulo {m} is:")
    print(f"[{a}] = {{ x | x ≡ {a} (mod {m}) }}")

def main():
    while True:
        residue_class()

        again = input("\nDo you want to try again? (yes/no): ").lower()

        if again != "yes":
            print("\nProgram ended.")
            break

main()