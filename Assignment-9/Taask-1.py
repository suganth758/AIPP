def sum_odd_and_even(number_list):
    # === Manual, Detailed Google Style Docstring ===
    """
    Calculates the separate sum of all odd numbers and the sum of all even numbers
    found within the input list.

    This function performs a single pass over the provided list, accumulating the
    sums of odd and even integers. It includes type checking and skips any
    non-integer elements with a console warning.

    Args:
        number_list (list): The list of numerical values (ideally integers) to be processed.

    Returns:
        tuple: A two-element tuple containing the results: (odd_sum, even_sum).
               The first element is the total sum of all odd integers, and the
               second element is the total sum of all even integers.

    Example:
        >>> sum_odd_and_even([1, 2, 3, 4, 5])
        (9, 6)
    """

    # === AI Copilot Generated Docstring (Simple/Concise) ===
    """
    Computes the sums of odd and even integers in `number_list`.

    Checks type consistency and aggregates sums. Returns a tuple of (odd_sum, even_sum).
    """

    odd_sum = 0
    even_sum = 0

    # Iterate through each number in the input list
    for number in number_list:
        # Check if the number is an integer to ensure the modulo operation works
        if isinstance(number, int):
            # If the number is perfectly divisible by 2, it's even
            if number % 2 == 0:
                even_sum += number
            # Otherwise, it's odd
            else:
                odd_sum += number
        else:
            # Optionally, skip non-integer values or raise an error
            print(f"Warning: Skipping non-integer value: {number}")

    return (odd_sum, even_sum)

# Example Usage:
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]

# Call the function
odd_total, even_total = sum_odd_and_even(my_numbers)

# Print the results
print(f"Original list: {my_numbers}")
print(f"Sum of odd numbers: {odd_total}")
print(f"Sum of even numbers: {even_total}")

# Another example:
another_list = [15, 22, 37, 48, 51, 60]
odd_total_2, even_total_2 = sum_odd_and_even(another_list)
print(f"\nOriginal list: {another_list}")
print(f"Sum of odd numbers: {odd_total_2}")
print(f"Sum of even numbers: {even_total_2}")