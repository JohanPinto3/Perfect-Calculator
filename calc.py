# Function definitions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def modulus(x, y):
    if y == 0:
        return "Error: Modulus by zero"
    return x % y

def power(x, y):
    return x ** y

def floor_divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x // y

# Operation mapping
operations = {
    '1': ('Add', add),
    '2': ('Subtract', subtract),
    '3': ('Multiply', multiply),
    '4': ('Divide', divide),
    '5': ('Modulus', modulus),
    '6': ('Power', power),
    '7': ('Floor Division', floor_divide)
}

# Display menu
def show_menu():
    print("\nSelect operation:")
    for key, (name, _) in operations.items():
        print(f"{key}. {name}")
    print("Type 'exit' to quit the calculator.\n")

# Calculator loop
while True:
    show_menu()
    choice = input("Enter choice (1-7 or 'exit'): ")

    if choice.lower() =='exit':
        print("Goodbye!")
        break

    if choice in operations:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        operation_name, operation_func = operations[choice]
        result = operation_func(num1, num2)
        print(f"{operation_name} Result: {num1} and {num2} => {result}")
    else:
        print("Invalid input. Please choose a valid option (1-7) or type 'exit'.")
