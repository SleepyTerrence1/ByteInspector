import FileReader as FReader
import FileTools as FTools

def Main():

    while True:
        print("\n=== Welcome to Byte Inspector V1 ===")
        print("------------------------------------")
        print("1. Read File")
        print("2. File Tools")
        print("Type 'exit' to quit.")


        CmdInput = input("/ >> ").strip()

        if CmdInput == "1":
            FReader.FileReader()

        elif CmdInput == "2":
            while True:
                print("\n=== File Tools ===")
                print("1. Find Text in File")
                print("2. Check File Integrity")
                print("3. Compare Two Files")
                print("4. Return to Main Menu")

                ToolInput = input("/ >> ").strip()

                if ToolInput == "1":
                    FTools.ByteFinder()

                elif ToolInput == "2":
                    FTools.FileIntegrityChecker()

                elif ToolInput == "3":
                    FTools.BinaryFileComparator()

                elif ToolInput == "4":
                    break

                else:
                    print("Invalid option.")

        elif CmdInput.lower() == "exit":
            print("Exiting program.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    Main()
