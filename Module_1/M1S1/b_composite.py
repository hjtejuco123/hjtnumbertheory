def get_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def is_composite(n):
    return n > 1 and len(get_factors(n)) > 2

def find_composites_up_to(limit):
    return [n for n in range(2, limit + 1) if is_composite(n)]

def simulate():
    print("=" * 65)
    print("                 COMPOSITE NUMBERS SIMULATION")
    print("=" * 65)
    print("Program Explanation")
    print("-" * 65)
    print("The program identifies composite numbers within a given range.")
    print("Composite numbers are natural numbers greater than 1 that have")
    print("more than two factors (i.e., they can be evenly divided by")
    print("numbers other than 1 and themselves).")
    print("=" * 65)

    while True:
        try:
            limit = int(input("\nEnter upper limit to find composites (e.g. 25): "))
            if limit < 4:
                print("Please enter a number >= 4 to see at least one composite.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    composites = find_composites_up_to(limit)

    print("\n" + "=" * 65)
    print("Output Analysis")
    print("=" * 65)
    print(f"\nInput:")
    print(f"  The user specifies an upper limit of {limit}. This means the")
    print(f"  program will check all numbers from 2 (the smallest composite")
    print(f"  number) up to {limit} to determine which are composite.")

    print(f"\nOutput:")
    print(f"  The program correctly lists all composite numbers between")
    print(f"  2 and {limit}. Let's verify this step-by-step:")

    print("\n" + "=" * 65)
    print("Verification of Composite Numbers")
    print("=" * 65)
    print("\nDefinition Recap:")
    print("  A composite number has more than two factors.")
    print("  For example, 4 is composite because its factors are [1, 2, 4].")

    print(f"\nNumbers Between 2 and {limit}:")
    print(f"\n  {'Number':<10} {'Factors':<40} {'Composite?'}")
    print("  " + "-" * 60)
    for n in range(2, limit + 1):
        factors = get_factors(n)
        composite = "Yes" if is_composite(n) else "No"
        print(f"  {n:<10} {str(factors):<40} {composite}")

    print("\n" + "=" * 65)
    print("Composite Numbers Identified:")
    print("=" * 65)
    print(f"\n  From the table above, the composite numbers between 2 and {limit} are:")
    print(f"\n  {composites}")
    print(f"\n  Total composite numbers found: {len(composites)}")
    print("\n" + "=" * 65)
    print("Simulation complete.")
    print("=" * 65)

if __name__ == "__main__":
    simulate()
