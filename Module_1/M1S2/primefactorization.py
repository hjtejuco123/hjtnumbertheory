# Prime Factorization with Simulation

def prime_factorization(n):
    original = n
    factor = 2
    factors = {}

    print("\n🔍 Step-by-step factorization:")

    while n > 1:
        if n % factor == 0:
            print(f"{n} ÷ {factor} = {n // factor}")
            
            if factor in factors:
                factors[factor] += 1
            else:
                factors[factor] = 1

            n = n // factor
        else:
            factor += 1  # move to next possible divisor

    # Display final result
    print("\nFinal Prime Factorization:")

    result = ""
    for f in factors:
        if factors[f] > 1:
            result += f"{f}^{factors[f]} × "
        else:
            result += f"{f} × "

    result = result[:-3]  # remove last " × "

    print(f"{original} = {result}")


# User Input
num = int(input("Enter a number greater than 1: "))

if num <= 1:
    print("Please enter a number greater than 1.")
else:
    prime_factorization(num)