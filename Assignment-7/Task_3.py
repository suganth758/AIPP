def divide_safe(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

print(divide_safe(10, 0))
print(divide_safe(10, 2))