def is_even_or_odd():
    print("\nWelcome to the Even and Odd Number Checker!")
    print("This program uses the formulas:")
    print(" - Even numbers: 2k")
    print(" - Odd numbers: 2k + 1\n")

    while True:
        print("Menu:")
        print("1. Check if a number is Even or Odd with Simulation")
        print("2. Generate Even Numbers")
        print("3. Generate Odd Numbers")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ").strip()
        
        if choice == '1':
            # Check if a number is even or odd 
            try:
                num = int(input("Enter a number to check: "))
                k = num // 2  # Integer division by 2
                if 2 * k == num:
                    print(f"{num} is an Even number.")
                    print(f"Simulation: {num} = 2 x {k}, {num} = {2 * k}\n")
                else:
                    print(f"{num} is an Odd number.")
                    print(f"Simulation: {num} = 2 x {k} + 1, {num} = {2 * k} + 1, {num} = {2 * k + 1}\n")
            except ValueError:
                print("Invalid input! Please enter an integer.\n")
        
        elif choice == '2':
            #  even numbers
            try:
                n = int(input("How many even numbers do you want to generate? "))
                if n <= 0:
                    print("Please enter a positive integer.\n")
                    continue
                print(f"First {n} Even numbers:")
                for k in range(n):
                    print(2 * k, end=" ")
                print("\n")
            except ValueError:
                print("Invalid input! Please enter an integer.\n")
        
        elif choice == '3':
            #  odd numbers
            try:
                n = int(input("How many odd numbers do you want to generate? "))
                if n <= 0:
                    print("Please enter a positive integer.\n")
                    continue
                print(f"First {n} Odd numbers:")
                for k in range(n):
                    print(2 * k + 1, end=" ")
                print("\n")
            except ValueError:
                print("Invalid input! Please enter an integer.\n")
        
        elif choice == '4':
            # Exit the program
            print("Thank you for using the Even and Odd Number Checker. Goodbye!")
            break
        
        else:
            # Invalid menu choice
            print("Invalid choice! Please select a valid option from the menu.\n")


if __name__ == "__main__":
    is_even_or_odd()