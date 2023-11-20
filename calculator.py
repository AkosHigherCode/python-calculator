def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract two numbers."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide two numbers."""
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def power(x, y):
    """Calculate the power of x to y."""
    return x ** y

def square_root(x):
    """Calculate the square root of a number."""
    if x >= 0:
        return x ** 0.5
    else:
        return "Error: Square root of a negative number"

def evaluate_expression(expression):
    """Evaluate a mathematical expression."""
    try:
        return eval(expression)
    except Exception as e:
        return f"Error: {e}"

def calculator():
    while True:
        print("\nPython Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Evaluate Expression")
        print("8. Exit")

        choice = input("Enter choice (1-8): ")

        if choice in ('1', '2', '3', '4', '5'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")
            elif choice == '5':
                print(f"Result: {power(num1, num2)}")

        elif choice == '6':
            num = float(input("Enter number: "))
            print(f"Result: {square_root(num)}")

        elif choice == '7':
            expression = input("Enter expression: ")
            print(f"Result: {evaluate_expression(expression)}")

        elif choice == '8':
            print("Exiting calculator...")
            break
        else:
            print("Invalid input")


calculator()
