def area_rectangle(length, width):
    return length * width

def area_square(side):
    return side * side

def area_circle(radius):
    return 3.14 * radius * radius

def calculate_area(shape, x, y=0):
    shapes = {
        "rectangle": lambda: area_rectangle(x, y),
        "square": lambda: area_square(x),
        "circle": lambda: area_circle(x)
    }
    return shapes.get(shape, lambda: "Invalid shape")()

# Example usage
print(calculate_area("rectangle", 10, 5))
print(calculate_area("square", 6))
print(calculate_area("circle", 4))