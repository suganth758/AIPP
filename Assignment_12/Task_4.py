import sympy
from sympy.abc import x

def analyze_cubic_function():
    """
    Analyzes f(x) = 2x^3 + 4x + 5. This function is strictly increasing
    and has no local minimum or maximum, as its derivative is always positive.
    """
    
    # Define the function
    f_x = 2*x**3 + 4*x + 5
    
    # Calculate the first derivative (f'(x))
    f_prime_x = sympy.diff(f_x, x)
    
    # Solve for critical points (where f'(x) = 0)
    critical_points = sympy.solve(sympy.Eq(f_prime_x, 0), x)
    real_critical_points = [p for p in critical_points if p.is_real]
    
    print(f"Function: f(x) = {f_x}")
    print(f"Derivative: f'(x) = {f_prime_x}")
    
    if not real_critical_points:
        print("\n--- Result ---")
        print("The function has NO real critical points (where the slope is zero).")
        print("Since f'(x) = 6x^2 + 4 is always positive, the function is strictly increasing.")
        print("It therefore has NO local minimum or maximum value.")
        print("Minimum value approaches -infinity as x approaches -infinity.")
    else:
        print(f"\nReal Critical Points found at x = {real_critical_points}")

if __name__ == "__main__":
    analyze_cubic_function()