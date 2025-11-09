def demonstrate_cm_to_inches(centimeters):
    """
    Demonstrates the conversion pattern from centimeters to inches
    1 inch = 2.54 centimeters
    
    Args:
        centimeters (float): Length in centimeters
        
    Returns:
        str: Description of the conversion pattern with example
    """
    inches = centimeters / 2.54
    
    pattern_description = f"""
    Conversion Pattern Demonstration:
    Input:  {centimeters} centimeters
    Output: {inches:.2f} inches
    Rule:   To convert centimeters to inches, divide by 2.54
    """
    
    return pattern_description

# Example usage
if __name__ == "__main__":
    example_input = 5.08  # 5.08 cm = 2 inches
    result = demonstrate_cm_to_inches(example_input)
    print(result)