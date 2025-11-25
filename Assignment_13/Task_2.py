def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found."
    except PermissionError:
        return "Error: Permission denied."
    except Exception as error:
        return f"Unexpected error: {error}"

# Main Program
filename = input("Enter filename: ")
output = read_file(filename)
print("Output:")
print(output)