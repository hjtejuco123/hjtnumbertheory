import math

def trial_division(n):
    print("\n========== TRIAL DIVISION SIMULATION ==========")

    if n <= 1:
        print(f"{n} is not prime because prime numbers must be greater than 1.")
        return False

    limit = int(math.sqrt(n))

    print(f"Input number: {n}")
    print(f"Square root of {n} = {math.sqrt(n):.2f}")
    print(f"Floor value = {limit}")
    print(f"We will test divisors from 2 to {limit}\n")

    for d in range(2, limit + 1):
        remainder = n % d
        print(f"Testing d = {d}")
        print(f"{n} mod {d} = {remainder}")

        if remainder == 0:
            print(f"\nSince {n} is divisible by {d},")
            print(f"{n} is COMPOSITE.")
            print(f"Smallest divisor found: {d}")
            return False
        else:
            print(f"{d} is not a divisor of {n}.\n")

    print(f"No divisor was found from 2 to {limit}.")
    print(f"Therefore, {n} is PRIME.")
    return True


def application_prime_key():
    print("\n========== APPLICATION: PRIME NUMBER KEY ==========")
    print("Prime numbers are used in cryptography.")
    print("This program checks if a number can be used as a simple prime key.\n")

    key = int(input("Enter a number to check as a prime key: "))

    is_prime = trial_division(key)

    if is_prime:
        print(f"\nAPPLICATION RESULT:")
        print(f"{key} can be used as a simple prime key.")
    else:
        print(f"\nAPPLICATION RESULT:")
        print(f"{key} should not be used as a prime key because it is not prime.")


def main():
    while True:
        print("\n========== PRIME NUMBER MENU ==========")
        print("1. Check if a number is prime")
        print("2. Application: Check prime key")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("\nEnter an integer greater than 1: "))
            trial_division(n)

        elif choice == "2":
            application_prime_key()

        elif choice == "3":
            print("Program ended. Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


main()