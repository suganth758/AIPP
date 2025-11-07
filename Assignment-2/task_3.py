import math
 
# --- 1. Define Calculation Functions for Each Shape ---
 
def calculate_square_area(side):
   """Area of a square: side * side"""
   return side * side
 
def calculate_circle_area(radius):
   """Area of a circle: pi * radius^2"""
   return math.pi * radius**2
 
def calculate_rectangle_area(length, width):
   """Area of a rectangle: length * width"""
   return length * width
 
def calculate_triangle_area(base, height):
   """Area of a triangle: 0.5 * base * height"""
   return 0.5 * base * height
 
# --- 2. Dictionary Dispatcher ---
 
# Maps shape names to their respective calculation function and required parameters.
SHAPE_CALCULATORS = {
   'square': {'func': calculate_square_area, 'params': ['side']},
   'circle': {'func': calculate_circle_area, 'params': ['radius']},
   'rectangle': {'func': calculate_rectangle_area, 'params': ['length', 'width']},
   'triangle': {'func': calculate_triangle_area, 'params': ['base', 'height']}
}
 
# --- 3. Main Dispatcher Function ---
 
def calculate_area(shape, **kwargs):
   """
   Calculates the area of a shape using a dictionary dispatcher.
   Example: calculate_area('rectangle', length=5, width=10)
   """
   shape = shape.lower()
 
   # Check if the requested shape is supported
   if shape not in SHAPE_CALCULATORS:
       return f"Error: Shape '{shape}' not supported."
 
   # Get the calculator details
   calculator = SHAPE_CALCULATORS[shape]
   func = calculator['func']
   required_params = calculator['params']
   
   # Check for required parameters
   args = {}
   for param in required_params:
       if param in kwargs:
           args[param] = kwargs[param]
       else:
           return f"Error: {shape.capitalize()} requires '{param}' dimension(s)."
 
   # Execute the calculation function with the collected arguments
   return func(**args)
 
# --- Example Usage ---
 
print(f"Square Area: {calculate_area('square', side=7)}")
print(f"Rectangle Area: {calculate_area('rectangle', length=8, width=5)}")
print(f"Triangle Area: {calculate_area('triangle', base=10, height=4)}")
print(f"Circle Error: {calculate_area('circle', radius_incorrect=3)}")