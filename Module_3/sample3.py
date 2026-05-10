# Properties of Congruence 
while True:

    print("\n========== MENU ==========")
    print("1. Reflexive Property")
    print("2. Symmetric Property")
    print("3. Transitive Property")
    print("4. Remainder Property")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # REFLEXIVE PROPERTY
    if choice == "1":

        print("\n=== REFLEXIVE PROPERTY ===")

        a = int(input("Enter a number a: "))
        m = int(input("Enter modulus m: "))

        difference = a - a

        print("\nStep 1: Subtract")
        print(a, "-", a, "=", difference)

        print("\nStep 2: Check divisibility by", m)
        print(difference, "÷", m, "=", difference // m)

        if difference % m == 0:
            print("\nSo:")
            print(a, "≡", a, "(mod", m, ")")
            print("TRUE")
        else:
            print("FALSE")

    # SYMMETRIC PROPERTY
    elif choice == "2":

        print("\n=== SYMMETRIC PROPERTY ===")

        a = int(input("Enter first number a: "))
        b = int(input("Enter second number b: "))
        m = int(input("Enter modulus m: "))

        difference = a - b

        print("\nStep 1: Subtract")
        print(a, "-", b, "=", difference)

        print("\nStep 2: Divide by", m)
        print(difference, "÷", m, "=", difference // m)

        if difference % m == 0:
            print("\nSo:")
            print(a, "≡", b, "(mod", m, ")")

            print("\nTherefore:")
            print(b, "≡", a, "(mod", m, ")")

            print("TRUE")
        else:
            print("FALSE")

    # TRANSITIVE PROPERTY
    elif choice == "3":

        print("\n=== TRANSITIVE PROPERTY ===")

        a = int(input("Enter first number a: "))
        b = int(input("Enter second number b: "))
        c = int(input("Enter third number c: "))
        m = int(input("Enter modulus m: "))

        print("\nChecking:")
        print(a, "≡", b, "(mod", m, ")")
        print("and")
        print(b, "≡", c, "(mod", m, ")")

        check1 = (a - b) % m
        check2 = (b - c) % m

        if check1 == 0 and check2 == 0:

            difference = a - c

            print("\nStep 1: Subtract")
            print(a, "-", c, "=", difference)

            print("\nStep 2: Divide by", m)
            print(difference, "÷", m, "=", difference // m)

            print("\nSo:")
            print(a, "≡", c, "(mod", m, ")")
            print("TRUE")

        else:
            print("\nThe conditions are not satisfied.")
            print("FALSE")

    # REMAINDER PROPERTY
    elif choice == "4":

        print("\n=== REMAINDER PROPERTY ===")

        a = int(input("Enter a number a: "))
        m = int(input("Enter modulus m: "))

        q = a // m
        r = a % m

        print("\nStep 1: Divide", a, "by", m)
        print(a, "÷", m, "=", q, "remainder", r)

        print("\nStep 2: Write using division algorithm")
        print(a, "=", q, "(", m, ") +", r)

        print("\nSo:")
        print(a, "≡", r, "(mod", m, ")")
        print("because the remainder is", r)

    # EXIT
    elif choice == "5":

        print("\nProgram terminated.")
        break

    # INVALID CHOICE
    else:
        print("\nInvalid choice. Please try again.")