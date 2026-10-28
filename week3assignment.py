
while True:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Mode (%)")
    print("5. Exponentiation (**)")
    print("6. Floor Division (//)")
    print("7. Division (/)")

    choice = int(input("Choose an operation (1-7): "))

    if choice == 1:
        print("Result:", a + b)
    elif choice == 2:
        print("Result:", a - b)
    elif choice == 3:
        print("Result:", a * b)
    elif choice == 4:
        if b != 0:
            print("Result:", a % b)
        else:
            print("Cannot divide by zero")
    elif choice == 5:
        print("Result:", a ** b)
    elif choice == 6:
        if b != 0:
            print("Result:", a // b)
        else:
            print("Cannot divide by zero")
    elif choice == 7:
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid choice")

    s = input("Do you want to continue? (yes/no): ")

    if s != "yes" and s != "YES":
        print("Calculator stopped.")
        break
