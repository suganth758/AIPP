def count_vowels(s, include_y=False):
    """
    Count vowels in a string (zero-shot). Returns 0 for None.
    
    Args:
        s: Value to count vowels in (will be converted to str).
        include_y (bool): If True, treat 'y' as a vowel.
    
    Returns:
        int: Number of vowels in the input.
    """
    if s is None:
        return 0
    s = str(s).lower()
    vowels = set("aeiou")
    if include_y:
        vowels.add("y")
    return sum(1 for ch in s if ch in vowels)