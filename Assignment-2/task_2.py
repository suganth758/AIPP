def is_palindrome(string):
    # Convert string to lowercase and remove non-alphanumeric characters
    cleaned_str = ''.join(char.lower() for char in string if char.isalnum())
    
    # Compare string with its reverse
    return cleaned_str == cleaned_str[::-1]

# Test cases
test_strings = [
    "A man, a plan, a canal: Panama",
    "race a car",
    "Was it a car or a cat I saw?",
    "hello",
    "12321"
]

for text in test_strings:
    print(f'"{text}" -> {is_palindrome(text)}')