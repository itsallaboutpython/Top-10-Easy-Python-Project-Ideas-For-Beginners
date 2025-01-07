print("===== Welcome to Calculator App =====\n")
while 1:
    print("What would you like to do:-")
    print("1. Addition")
    print("2. Subtraction")
    print("3  Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if choice == 1:    
        print("Output: ", num1+num2)
    elif choice == 2:
        print("Output: ", num1-num2)
    elif choice == 3:
        print("Output: ", num1*num2)
    elif choice == 4:
        print("Output: ", num1/num2)
    elif choice == 5:
        print("Exiting...")
        break
    print()
