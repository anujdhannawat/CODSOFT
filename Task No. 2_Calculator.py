def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

print("CodSoft Calculator Application\n")
print("Select operation you want to perorm:\n")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division\n")

while True:
    choice = input("Enter your choice: ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))

        if choice == '1':
            print("Result:", num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print("Result:", num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print("Result:", num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print("Result:", num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid input")
