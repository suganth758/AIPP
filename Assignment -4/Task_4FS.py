def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Testing the examples
print(count_vowels("apple"))      # 2
print(count_vowels("hello"))      # 2
print(count_vowels("education"))  # 5
print(count_vowels("sky"))        # 01