def successor(n):
    return n + 1


def visualize_addition(m, n):
    print("\nVISUALIZATION (Building using Successor):\n")

    current = m
    print(f"Start: {current}")

    for i in range(1, n + 1):
        next_val = successor(current)

        print(f"Step {i}: S({current}) = {current} + 1 = {next_val}")
        print("         " + "↑ (successor applied)\n")

        current = next_val

    print(f"Final Answer: {m} + {n} = {current}")
    return current


# Main program
print("SUCCESSOR OPERATION VISUALIZATION")
print("---------------------------------")

m = int(input("Enter first number (m): "))
n = int(input("Enter second number (n): "))

# Show simple successor first
print("\nBasic Successor:")
print(f"S({m}) = {successor(m)}")
print(f"S({n}) = {successor(n)}")

# Visualization
visualize_addition(m, n)