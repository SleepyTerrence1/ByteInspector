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
            content = file.read()
            print("File content:")
            print(len(content))

            number = int(input("Enter the number of bytes to display (in hex): "))

            print(content[:number].hex())
            try:
                for key, value in File_Signatures.items():
                    if content.startswith(value):
                        print(f"File Type: {key}")
                        break
                else:
                    print("File Type: Unknown")
            except Exception as e:
                print(f"An error occurred while determining the file type: {e}")
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")

FileReader()