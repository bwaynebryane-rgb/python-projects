print("Welcome To Brian School Helper")

while True:
    print("1. Calculator")
    print("2. Grade Checker")
    print("3. Age Checker")
    print("4. Exit")
    choice = input("Pick 1, 2, 3 or 4: ")

    if choice == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Addition:", num1 + num2)
        print("Subtraction:", num1 - num2)
        print("Multiplication:", num1 * num2)
        if num2 != 0:
            print("Division:", num1 / num2)
        else:
            print("cannot divide by zero")

    elif choice == "2":
        marks = float(input("Enter your marks out of 100: "))
        if marks >= 80:
            print("Grade A - Excellent!")
        elif marks >= 60:
            print("Grade B - Good!")
        elif marks >= 40:
            print("Grade C - Pass")
        else:
            print("Grade D - Try Again")

    elif choice == "3":
        age = int(input("Enter your age: "))
        if age >= 18:
            print("You are an Adult")
        else:
            print("You are a Student")

    elif choice == "4":
        print("Thanks Brian! Bye!")
        break
    else:
        print("Pick 1, 2, 3 or 4 only")
