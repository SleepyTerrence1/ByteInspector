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

            number = int(input("Enter the number of bytes to display (in hex):"))

            print(content[:number].hex())

            for i in File_Signatures.items():
                if content.startswith(File_Signatures[i]):
                    print(f"File Type: {i}")
                    break
                else:
                    return print("File Type: Unknown")
            """
            if content.startswith(File_Signatures["JPEG"]):
                print("File Type: JPEG")
            elif content.startswith(File_Signatures["GIF"]):
                print("File Type: GIF")
            elif content.startswith(File_Signatures["PNG"]):
                print("File Type: PNG")
            elif content.startswith(File_Signatures["PDF"]):
                print("File Type: PDF")
            else:
                print("File Type: Unknown")
            """
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")

FileReader()