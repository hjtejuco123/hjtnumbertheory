# Program to compute factorial (n!) with simulation

def factorial_simulation(n):
    product = 1
    
    print("\n--- PROGRAM SIMULATION ---")
    print(f"Factorial: {n}! = {n} × ({n-1}) × ... × 1\n")
    
    expression = ""  # to build expression string
    
    for i in range(n, 0, -1):
        print(f"Step: Multiply by {i}")
        product *= i
        
        #  expression display
        if i > 1:
            expression += f"{i} × "
        else:
            expression += f"{i}"
    
    print("\nExpanded Expression:")
    print(expression)
    
    print("\nFinal Answer:")
    print(f"{n}! = {product}")
    
    return product


# --- USER INPUT ---
n = int(input("Enter a positive integer: "))

# Call function
factorial_simulation(n)