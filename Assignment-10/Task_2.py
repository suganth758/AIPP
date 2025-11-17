def find_common(a, b):
    """Returns common elements between two lists using set intersection."""
    return list(set(a) & set(b))


# ---------------------------------------------------------
# Example Usage / Test Calls
# ---------------------------------------------------------
if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]

    print("Common Elements:", find_common(list1, list2))
