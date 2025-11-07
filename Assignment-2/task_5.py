def sum_even_odd(numbers):
    """Return a dict with sums of even and odd integers from the iterable `numbers`."""
    even_sum = 0
    odd_sum = 0
    for n in numbers:
        if not isinstance(n, int):
            raise TypeError("All items in 'numbers' must be integers")
        if n % 2 == 0:
            even_sum += n
        else:
            odd_sum += n
    return {'even': even_sum, 'odd': odd_sum}

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = sum_even_odd(nums)
    print(f"Even sum: {result['even']}")  # Even sum: 30
    print(f"Odd sum: {result['odd']}")    # Odd sum: 25