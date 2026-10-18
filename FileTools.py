import hashlib

def ByteFinder():
    file_path = input("Enter a file path: ")
    search_text = input("Enter text to search for: ")


    try:
        with open(file_path, "rb") as file:
            content = file.read()

        search_bytes = search_text.encode("utf-8")
        position = content.find(search_bytes)

        if position != -1:
            print(f"Match found at offset: {position:08X}")
        else:
            print("No match found.")

    except FileNotFoundError:
        print("Error: File not found.")


def FileIntegrityChecker():
    file_path = input("Enter a file path: ")


    try:
        sha256 = hashlib.sha256()

        with open(file_path, "rb") as file:
            while True:
                chunk = file.read(4096)

                if not chunk:
                    break

                sha256.update(chunk)

        print("SHA-256:", sha256.hexdigest())

    except FileNotFoundError:
        print("Error: File not found.")


    def BinaryFileComparator():
        file1_path = input("Enter the first file path: ")
        file2_path = input("Enter the second file path: ")


        try:
            with open(file1_path, "rb") as file1:
                data1 = file1.read()

            with open(file2_path, "rb") as file2:
                data2 = file2.read()

            if data1 == data2:
                print("The files are identical.")
            else:
                print("The files are different.")

        except FileNotFoundError:
            print("Error: One or both files could not be found.")