import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def least_residue_program():
    clear_screen()

    print("=" * 45)
    print("          LEAST RESIDUE PROGRAM")
    print("=" * 45)

    # User input
    a = int(input("Enter the number a: "))
    m = int(input("Enter the modulo m: "))

    # Validation
    if m <= 0:
        print("\nError: Modulo must be a positive integer.")
        return

    # Computation
    quotient = a // m
    remainder = a % m

    print("\n" + "=" * 45)
    print("GIVEN")
    print("=" * 45)
    print(f"Find the least residue of {a} modulo {m}")
    print(f"Expression: {a} (mod {m})")

    print("\nMeaning:")
    print(f"We divide {a} by {m}.")
    print("The remainder is called the least residue.")

    print("\nPossible least residues:")
    print(f"0 to {m - 1}")

    print("\n" + "=" * 45)
    print("STEP 1: DIVIDE")
    print("=" * 45)
    print(f"{a} ÷ {m} = {quotient} remainder {remainder}")

    print("\nExplanation:")
    print(f"{m} goes into {a} exactly {quotient} time(s).")
    print(f"The leftover value is {remainder}.")

    print("\n" + "=" * 45)
    print("STEP 2: USE THE DIVISION FORMULA")
    print("=" * 45)
    print("Formula:")
    print("a = qm + r")

    print("\nSubstitution:")
    print(f"a = {a}")
    print(f"q = {quotient}")
    print(f"m = {m}")
    print(f"r = {remainder}")

    print("\nSo:")
    print(f"{a} = ({quotient})({m}) + {remainder}")
    print(f"{a} = {quotient * m} + {remainder}")
    print(f"{a} = {quotient * m + remainder}")

    print("\n" + "=" * 45)
    print("STEP 3: WRITE AS CONGRUENCE")
    print("=" * 45)
    print(f"Since the remainder is {remainder}:")
    print(f"{a} ≡ {remainder} (mod {m})")

    print("\nMeaning:")
    print(f"{a} and {remainder} have the same remainder when divided by {m}.")

    print("\n" + "=" * 45)
    print("STEP 4: VERIFY THE ANSWER")
    print("=" * 45)
    difference = a - remainder
    verify_q = difference // m
    verify_r = difference % m

    print("To verify congruence, subtract:")
    print(f"{a} - {remainder} = {difference}")

    print("\nNow check if the difference is divisible by the modulo:")
    print(f"{difference} ÷ {m} = {verify_q} remainder {verify_r}")

    if verify_r == 0:
        print("\nBecause the remainder is 0, the difference is divisible by the modulo.")
        print(f"Therefore, {a} ≡ {remainder} (mod {m}) is TRUE.")
    else:
        print("\nThe difference is not divisible by the modulo.")
        print("So the congruence is FALSE.")

    print("\n" + "=" * 45)
    print("STEP 5: SHOW ALL POSSIBLE LEAST RESIDUES")
    print("=" * 45)

    print(f"For modulo {m}, the possible least residues are:")
    for i in range(m):
        print(i, end=" ")
    print()

    print("\nExplanation:")
    print(f"A remainder must be greater than or equal to 0")
    print(f"and less than {m}.")
    print(f"So the remainder must be from 0 to {m - 1}.")

    print("\n" + "=" * 45)
    print("STEP 6: SIMPLE SIMULATION")
    print("=" * 45)

    print(f"Let us divide some numbers by {m}:\n")

    for i in range(m):
        sample = m + i
        q = sample // m
        r = sample % m

        print(f"{sample} ÷ {m} = {q} remainder {r}")

    print("\nNotice:")
    print(f"The remainders repeat from 0 up to {m - 1}.")

    print("\n" + "=" * 45)
    print("FINAL ANSWER")
    print("=" * 45)
    print(f"Least residue = {remainder}")
    print(f"Final congruence: {a} ≡ {remainder} (mod {m})")


def main():
    while True:
        least_residue_program()

        again = input("\nDo you want to try again? (yes/no): ").lower()

        if again != "yes":
            print("\nProgram ended.")
            break


main()