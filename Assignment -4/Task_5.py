def count_lines_in_file(file_path):
    """
    Count total number of lines in a text file.

    Args:
        file_path (str): Task_5.txt.

    Returns:
        int: Number of lines.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)