def fibonacci_r(n):
    """
    Recursively calculates the nth Fibonacci number.
    fibonacci_r(0) = 0
    fibonacci_r(1) = 1
    fibonacci_r(n) = fibonacci_r(n-1) + fibonacci_r(n-2) for n > 1
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_r(n - 1) + fibonacci_r(n - 2)

# Example usage:
if __name__ == "__main__":
    n = int(input("Enter n: "))
    print(f"The {n}th Fibonacci number is {fibonacci_r(n)}")