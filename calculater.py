def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y):
    return x / y if y != 0 else "Cannot divide by zero"

print("Select operation:")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

choice = input("Enter choice: ")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

operations = {"1": add, "2": sub, "3": mul, "4": div}
result = operations.get(choice, lambda a,b: "Invalid choice")(x, y)
print("Result:", result)
