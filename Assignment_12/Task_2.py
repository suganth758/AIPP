def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Sample list
data = [64, 34, 25, 12, 22, 11, 90]

# Keep a copy of the original data for printing
original_data = list(data)

# Sort the data
sorted_data = bubble_sort(data)

# Print the original and sorted data
print(f"Original array: {original_data}")
print(f"Sorted array: {sorted_data}")