def sum_of_squares(nums):
    """Return the sum of squares of the numbers in `nums`."""
    return sum(x * x for x in nums)

# Example usage
values = [1, 2, 3, 4]
result = sum_of_squares(values)
print(result)  # 30