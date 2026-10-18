import FileReader as FReader

def Main():
    print("=== Welcome to Byte Inspector V1 ===")
    print("------------------------------------")
    print("")
    print("Choose a option:")
    print("1. Read File")
    print("")
    print("Type 'exit' to quit the program.")
    while True:
        CmdInput = input("/ >> ")
        if CmdInput == "1":
            FReader.FileReader()
        elif CmdInput.lower() == "exit":
            print("Exiting program.")
            break

Main()