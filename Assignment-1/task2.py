def is_prime(n: int) -> bool:
    """Return True if integer n is prime, otherwise False."""
    import math

    if not isinstance(n, int):
        return False
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = math.isqrt(n)
    i = 3
    while i <= limit:
        if n % i == 0:
            return False
        i += 2
    return True


if __name__ == "__main__":
    # quick manual tests
    samples = [-1, 0, 1, 2, 3, 4, 17, 18, 19, 97, 100]
    print({n: is_prime(n) for n in samples})