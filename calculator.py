print("===== Welcome to Calculator App =====\n")
while 1:
    print("What would you like to do:-")
    print("1. Addition")
    print("2. Subtraction")
    print("3  Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Output: ", num1+num2)
    elif choice == 2:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Output: ", num1-num2)
    elif choice == 3:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Output: ", num1*num2)
    elif choice == 4:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Output: ", num1/num2)
    elif choice == 5:
        print("Exiting...")
        break
    print()