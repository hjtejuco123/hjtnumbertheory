# Program to compute product of (2k) from k = 1 to n

def product_simulation(n):
    product = 1
    
    print("\n--- PROGRAM SIMULATION ---")
    print(f"Product: Π (2k), from k = 1 to k = {n}\n")
    
    expression = ""  # to build expression string
    
    for k in range(1, n + 1):
        value = 2 * k
        
        #  step computation
        print(f"Step {k}: 2({k}) = {value}")
        
        product *= value
        
        #  expression display
        if k < n:
            expression += f"{value} × "
        else:
            expression += f"{value}"
    
    print("\nExpanded Expression:")
    print(expression)
    
    print("\nFinal Answer:")
    print(f"Product = {product}")
    
    return product


# --- USER INPUT ---
n = int(input("Enter the value of n (upper limit): "))

# Call function
product_simulation(n)