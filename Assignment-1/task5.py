from typing import Iterable, Any


def find_max(values: Iterable[Any]) -> Any:
    """Return the largest element from values.
    Raise ValueError on empty iterable."""
    it = iter(values)
    try:
        current_max = next(it)
    except StopIteration:
        raise ValueError("find_max() arg is an empty iterable")

    for v in it:
        if v > current_max:
            current_max = v
    return current_max


if __name__ == "__main__":
    samples = [
        [3, 1, 4, 1, 5, 9],
        [-10, -3, -20],
        [42],
    ]
    for s in samples:
        print(s, "->", find_max(s))
