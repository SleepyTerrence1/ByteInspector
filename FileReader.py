file_path = input("Enter a file path: ")

try:
    with open(file_path) as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file at '{file_path}' was not found.")