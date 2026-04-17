#Fermat Little Theorem 

def is_prime(n):
    if n <= 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#user input
a = int(input("Enter a value for a: "))
p = int(input("Enter a prime number: "))

if not is_prime(p):
    print("\nError: p must be a prime number.")
elif a%p == 0:
    print("\nError: a must not be divisible by p.")
else:
    exponent = p - 1
    power_value = a ** exponent
    remainder = power_value % p

    print ("\nSimulation of Fermat's Little Theorem:")
    print (f"Given a = {a} and prime p = {p})")
    print (f"Formula: a^(p-1) ≡ 1 (mod p)")
    print (f"Step 1: Calculate p-1 mod p ={exponent}")
    print (f"Step 2: {a}^{exponent} = {power_value}")
    print (f"Step 3: {power_value} mod {p} = {remainder}")

    if remainder == 1:
        print ("\nResult: Fermat's Little Theorem holds true, as {a}^(p-1) ≡ 1 (mod {p}).")
    else:
        print ("\nResult: Fermat's Little Theorem does not hold, as {a}^(p-1) ≡ {remainder} (mod {p}).")