import hashlib

def Tools():
    file_path = input("Enter a file path: ")
    File_Signatures = {
        "JPEG": bytes.fromhex("FFD8FF"),
        "PNG": bytes.fromhex("89504E470D0A1A0A"),
        "GIF": bytes.fromhex("47494638"),
        "PDF": bytes.fromhex("25504446"),
    }


    def ByteFinder():
        pass
    def FileIntegrityChecker():
        try:
            def CalculateFileHash(file_path):
                sha256 = hashlib.sha256()

                with open(file_path, "rb") as file:
                    while True:
                        chunk = file.read(4096)

                        if not chunk:
                            break

                        sha256.update(chunk)
                return sha256.hexdigest()
        except FileNotFoundError:
            print(f"Error: The file at '{file_path}' was not found.")
    def BinaryFileComparator():
        pass
#Finish after Terra ends