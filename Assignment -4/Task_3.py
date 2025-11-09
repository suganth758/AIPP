def format_name(first_name, last_name):
    """
    Formats a full name as "Last, First"
    
    Args:
        first_name (str): Person's first name
        last_name (str): Person's last name
        
    Returns:
        str: Formatted name as "Last, First"
    """
    if not first_name or not last_name:
        return "Invalid input: Both first and last names are required"
        
    # Strip any extra whitespace and capitalize first letters
    first_name = first_name.strip().capitalize()
    last_name = last_name.strip().capitalize()
    
    return f"{last_name}, {first_name}"

# Example usage
if __name__ == "__main__":
    print(format_name("john", "doe"))  # Output: Doe, John
    print(format_name("JANE", "SMITH"))  # Output: Smith, Jane