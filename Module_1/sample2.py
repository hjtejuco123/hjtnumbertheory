#Seive of Erasthosthenes 
def seive_of_erasthosthenes(n):
    prime = [True] * (n+1)
    if n >= 0:
        prime[0] = False
    if n >= 1:
        prime[1] = False
    
    print ("\nPrime numbers from 0 to ", n, ":")
    for i in range(n+1):
        print(i, end=" ")
    print()

    p = 2
    while (p * p <= n):
        if (prime[p]):
            print(f"\n{p} is prime, so mark its multiples as non-prime:")
            for i in range(p * p, n+1, p):
                if prime[i]:
                    prime[i] = False
                    print(f"Mark {i} as non-prime")
        p += 1
    
    primes = []
    for i in range(2, n+1):
        if prime[i]:
            primes.append(i)
    return primes

#user input
n = int(input("Enter a number: "))

if n < 2:
    print("\nNumbers from 0 to ", n, ":")
    for i in range(n+1):
        print(i, end=" ")
    print("\nNo prime numbers in this range.")
else:
    result = seive_of_erasthosthenes(n)
    print("\nPrime numbers are:")
    for prime in result:
        print(prime, end=" ")
    print()