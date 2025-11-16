def reverse_string(s: str) -> str:
    """Return the reversed version of the input string."""
    if not isinstance(s, str):
        raise TypeError("reverse_string expects a str")
    return s[::-1]


if __name__ == "__main__":
    samples = ["hello", "", "racecar", "12345"]
    print({s: reverse_string(s) for s in samples})