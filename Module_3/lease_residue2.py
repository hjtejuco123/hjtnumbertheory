import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def least_residue():

    clear_screen()

    print("===================================")
    print("      LEAST RESIDUE PROGRAM")
    print("===================================")

    # USER INPUT
    a = int(input("Enter the number a: "))
    m = int(input("Enter the modulo m: "))

    # VALIDATION
    if m <= 0:
        print("\nModulo must be a positive integer.")
        return

    # COMPUTATION
    quotient = a // m
    remainder = a % m

    print("\n===================================")
    print("Given")
    print("===================================")

    print(f"\nFind the least residue of:")
    print(f"{a} (mod {m})")

    print("\nDefinition:")
    print("The least residue is the remainder")
    print("when a is divided by m.")

    print("\nPossible least residues are:")
    print(f"0, 1, 2, ..., {m-1}")

    # STEP 1
    print("\n===================================")
    print("Step 1: Divide")
    print("===================================")

    print(f"\n{a} ÷ {m} = {quotient} remainder {remainder}")

    # STEP 2
    print("\n===================================")
    print("Step 2: Division Algorithm")
    print("===================================")

    print("\nFormula:")
    print("a = qn + r")

    print("\nWhere:")
    print(f"a = {a}")
    print(f"q = {quotient}")
    print(f"n = {m}")
    print(f"r = {remainder}")

    print("\nSubstitute the values:")

    print(f"{a} = ({quotient})({m}) + {remainder}")

    multiplication = quotient * m

    print(f"{a} = {multiplication} + {remainder}")

    print(f"{a} = {a}")

    # STEP 3
    print("\n===================================")
    print("Step 3: Congruence Form")
    print("===================================")

    print(f"\nSince the remainder is {remainder},")

    print(f"{a} ≡ {remainder} (mod {m})")

    # STEP 4
    print("\n===================================")
    print("Step 4: Verify Using Difference")
    print("===================================")

    difference = a - remainder

    print(f"\nSubtract the least residue from the original number:")

    print(f"{a} - {remainder} = {difference}")

    verify_q = difference // m
    verify_r = difference % m

    print(f"\nNow divide the difference by {m}:")

    print(f"{difference} ÷ {m} = {verify_q} remainder {verify_r}")

    if verify_r == 0:
        print("\nSince the remainder is 0,")
        print(f"{difference} is divisible by {m}.")
        print("Therefore:")
        print(f"{a} ≡ {remainder} (mod {m})")
        print("TRUE.")
    else:
        print("\nFALSE.")

    # STEP 5
    print("\n===================================")
    print("Step 5: Possible Least Residues")
    print("===================================")

    print(f"\nFor modulo {m},")

    print("the only possible least residues are:\n")

    for i in range(m):
        print(i, end=" ")

    print()

    print("\nExplanation:")
    print(f"When dividing by {m},")
    print(f"the remainder must always be between")
    print(f"0 and {m-1}.")

    # STEP 6
    print("\n===================================")
    print("Step 6: Simulation")
    print("===================================")

    print(f"\nExamples of division by {m}:\n")

    for i in range(m):

        sample = m + i

        q = sample // m
        r = sample % m

        print(f"{sample} ÷ {m} = {q} remainder {r}")

    # FINAL ANSWER
    print("\n===================================")
    print("Final Answer")
    print("===================================")

    print(f"\nLeast residue: {remainder}")

    print(f"\nFinal Congruence:")
    print(f"{a} ≡ {remainder} (mod {m})")


def main():

    while True:

        least_residue()

        again = input("\nDo you want to try again? (yes/no): ").lower()

        if again != "yes":
            print("\nProgram ended.")
            break


main()