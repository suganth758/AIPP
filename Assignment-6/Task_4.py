def sum_to_n(n):
    """
    Calculates the sum of the first n positive integers using the 
    mathematical formula: n * (n + 1) / 2.
    
    This method is highly efficient (O(1) complexity).

    :param n: The last number in the sequence (int).
    :return: The sum of numbers from 1 to n (int).
    """
    if not isinstance(n, int) or n < 1:
        # Handle non-integer or non-positive input gracefully
        return 0
        
    # The // operator ensures integer division, resulting in an integer sum
    return n * (n + 1) // 2
# Calculate the sum of the first 5 numbers (1 + 2 + 3 + 4 + 5)
result_5 = sum_to_n(5) 
print(f"The sum of the first 5 numbers is: {result_5}")

# Calculate the sum of the first 10 numbers (1 + 2 + ... + 10)
result_10 = sum_to_n(10)
print(f"The sum of the first 10 numbers is: {result_10}")

# Calculate the sum of the first 100 numbers
result_100 = sum_to_n(100)
print(f"The sum of the first 100 numbers is: {result_100}")