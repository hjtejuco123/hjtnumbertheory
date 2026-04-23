# Program to compute summation of (2n - 1) from n = 1 to k

def summation_simulation(k):
    total = 0
    
    print("\n--- PROGRAM SIMULATION ---")
    print(f"Summation: Σ (2n - 1), from n = 1 to n = {k}\n")
    
    expression = ""  # to build expression string
    
    for n in range(1, k + 1):
        value = 2 * n - 1
        
        #  step computation
        print(f"Step {n}: 2({n}) - 1 = {value}")
        
        total += value
        
        #  expression display
        if n < k:
            expression += f"{value} + "
        else:
            expression += f"{value}"
    
    print("\nExpanded Expression:")
    print(expression)
    
    print("\nFinal Answer:")
    print(f"Total = {total}")
    
    return total


# --- USER INPUT ---
k = int(input("Enter the value of n (upper limit): "))

# Call function
summation_simulation(k)