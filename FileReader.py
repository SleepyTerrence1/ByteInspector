def FileReader():

    file_path = input("Enter a file path: ")
    File_Signatures = {
        "JPEG": bytes.fromhex("FFD8FF"),
        "PNG": bytes.fromhex("89504E470D0A1A0A"),
        "GIF": bytes.fromhex("47494638"),
        "PDF": bytes.fromhex("25504446"),
    }
    try:
        with open(file_path, "rb") as file:
            print("File content:")
            print(f"File Size: {len(content)} bytes")
            try:
                number = int(input("Enter the number of bytes to display (in hex): "))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                return

            if number < 0:
                print("Invalid input. Please enter a non-negative integer.")
                return

            print(f"Bytes(in hex): {content[:number].hex()}")

            for key, value in File_Signatures.items():
                if content.startswith(value):
                    print(f"File Type: {key}")
                    break
            else:
                print("File Type: Unknown")
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")

FileReader()