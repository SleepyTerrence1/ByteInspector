file_path = input("Enter a file path: ")

try:
    with open(file_path, "rb") as file:
        content = file.read()
        print("File content:")
        print(len(content))
        print(content.hex)
except FileNotFoundError:
    print(f"Error: The file at '{file_path}' was not found.")