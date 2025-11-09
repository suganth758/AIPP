def is_leap_year(year):
    """
    Check if the given year is a leap year.
    
    Args:
        year (int): The year to check
    
    Returns:
        bool: True if it's a leap year, False otherwise
    """
    if year <= 0:
        return False
        
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False