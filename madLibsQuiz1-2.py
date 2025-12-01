def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

print("Do you want to do an addition or subtraction problem?")
choice = input("Type 'add' for addition or 'subtract' for subtraction: ").lower()

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == "add":
    result = add_numbers(num1, num2)
    print(f"The result of adding {num1} and {num2} is {result}.")

elif choice == "subtract":
    result = subtract_numbers(num1, num2)
    print(f"The result of subtracting {num2} from {num1} is {result}.")

else:
    print("Invalid choice. Please run the program again.")

