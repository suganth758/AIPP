numbers = [1, 2, 3]
index_to_access = 5 # This is still the invalid index that will cause the error

try:
    # Attempt the access
    print(numbers[index_to_access])
    
except IndexError:
    # Handle the error specifically
    print(f"Error: The list index {index_to_access} is out of range.")
    print(f"Valid indices are 0 to {len(numbers) - 1}.")
    
except Exception as e:
    # Handle any other unexpected error
    print(f"An unexpected error occurred: {e}")