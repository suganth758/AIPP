def calculate_total_sum(numbers_list):
    """
    Calculates the total sum of all elements in a list of numbers.

    Args:
        numbers_list (list): A list containing integers or floats.

    Returns:
        int/float: The total sum of all numbers in the list.
    """
    total = 0
    # Loop through each number and add it to the total
    for number in numbers_list:
        total += number
    return total

# --- Example Usage ---
data = [10, 25, 3.5, 7, 1]

# Calculate the sum
result = calculate_total_sum(data)

# Print the final result
print(f"The list is: {data}")
print(f"The total sum is: {result}")