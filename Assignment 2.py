def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        try:
            choice = int(input("Enter your choice (1/2/3/4): "))
            if choice in [1, 2, 3, 4]:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        result = add(num1, num2)
    elif choice == 2:
        result = subtract(num1, num2)
    elif choice == 3:
        result = multiply(num1, num2)
    else:
        result = divide(num1, num2)

    print(f"The result is: {result}")
    return result

def display_history(history):
    print("\nCalculation history:")
    for i, operation in enumerate(history, 1):
        print(f"{i}. {operation}")

if __name__ == "__main__":
    calculation_history = []
    while True:
        calculator()
        should_continue = input("Do you want to perform another calculation? (yes/no): ")
        if should_continue.lower() != "yes":
            break
        calculation_history.append(f"{calculation_history[-1]} + {input('Enter the next operation: ')}")
    display_history(calculation_history)