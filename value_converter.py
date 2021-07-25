def convert_temperature():
    print("\nWhich conversion do you want to choose:-")
    print("1. Celsius to Faranheit")
    print("2. Faranheit to Celsius")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        temp = float(input("Enter temperature in celsius: "))
        print(f"{temp} degree celsius is equal to {(temp*9/5)+32} degree faranheit.\n")
    elif choice == 2:
        temp = float(input("Enter temperature in faranheit: "))
        print(f"{temp} degree faranheit is equal to {(temp-32)*5/9} degree celsius.\n")
    else:
        print("Invalid input...please try again\n")

def convert_currency():
    print("\nWhich conversion do you want to choose:-")
    print("1. Dollar to pound")
    print("2. Pound to Dollar")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = float(input("Enter currency in dollars: "))
        print(f"{value} dollars in pounds will be {value*0.73}\n")
    elif choice == 2:
        value = float(input("Enter currency in pounds: "))
        print(f"{value} pounds in dollars will be {value/0.73}\n")

def convert_lengths():
    print("\nWhich conversion do you want to choose:-")
    print("1. Centimeters to foot and inches")
    print("2. Foot and inches to centimeter")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = float(input("Enter length in cm: "))
        inches = value/2.54
        feet = inches/12
        print(f"{value} centimeters in equal to {feet} feet and {inches} inch\n")
    elif choice == 2:
        feet = float(input("Enter length in feet: "))
        inches = float(input("Enter length in inches: "))
        length = (feet*12 + inches)*2.54
        print(f"{feet} feet and {inches} inches in centimeters will be {length}\n")

print("===== Welcome to Value Converter =====")
while 1:
    print("Which option would you like to choose:-")
    print("1. Convert temperature")
    print("2. Convert currency")
    print("3. Convert lengths")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        convert_temperature()
    elif choice == 2:
        convert_currency()
    elif choice == 3:
        convert_lengths()
    elif choice == 4:
        print('Exiting...')
        exit(0)