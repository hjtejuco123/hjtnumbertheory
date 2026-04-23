# Prime Number Generation using Sieve of Eratosthenes
# With step-by-step simulation

def display_numbers(numbers, crossed_out):
    """Display numbers from 2 to n, marking crossed out numbers with X."""
    for num in numbers:
        if num in crossed_out:
            print(f"{num:>2}X", end="   ")
        else:
            print(f"{num:>2}", end="    ")
    print("\n")


def sieve_with_simulation(n):
    if n < 2:
        print("There are no prime numbers less than 2.")
        return

    numbers = list(range(2, n + 1))
    crossed_out = set()

    print("\nPRIME NUMBER GENERATION")
    print(f"Algorithm Trace: Sieve of n = {n}")
    print(f"Goal: Find all primes <= {n}")
    print("\nStep 1: Start with an array of numbers 2 through", n)
    display_numbers(numbers, crossed_out)

    p = 2
    step = 2

    while p * p <= n:
        if p not in crossed_out:
            print(f"Step {step}: p = {p}")
            print(f"Keep {p}, cross out its multiples:")

            crossed_this_step = []

            for multiple in range(p * 2, n + 1, p):
                if multiple not in crossed_out:
                    crossed_out.add(multiple)
                    crossed_this_step.append(multiple)

            if crossed_this_step:
                print("Crossed out:", crossed_this_step)
            else:
                print("No new multiples to cross out.")

            display_numbers(numbers, crossed_out)
            step += 1

        # Move to the next uncrossed number
        p += 1
        while p <= n and p in crossed_out:
            p += 1

    # Remaining uncrossed numbers are primes
    primes = [num for num in numbers if num not in crossed_out]

    print(f"Step {step}: Remaining uncrossed numbers are prime.")
    print("Prime numbers are:", primes)


# Main Program
print("=== Prime Number Generator ===")
n = int(input("Enter a value for n: "))
sieve_with_simulation(n)