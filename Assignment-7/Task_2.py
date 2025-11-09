def count_down(n):
    # Check if the input is a non-negative integer for a meaningful countdown
    if not isinstance(n, int) or n < 0:
        print("Please provide a non-negative integer.")
        return
        
    print(f"Starting countdown from {n}:")
    while n >= 0:
        print(n)
        # FIX: Decrement n by 1 to move towards the loop's termination condition (n=0)
        n -= 1 

# Example of how to use the fixed function
count_down(5)