import modules


def main():

    while True:

        print("\n"+"="*30)

        print("Welcom to Multi-Utility Toolkit")

        print("="*30)

        print("\n Choose an option:")
        print("1.Datetime and Time operations")
        print("2.Mathematical Operations")
        print("3.Random Data Generation")
        print("4.Generate Unique Identifiers(UUID)")
        print("5.File Operations(Custom Module)")
        print("6.Explore Module Attributes(dir())")
        print("7.exit")

        ch = int(input("Enter your choice:"))

        if ch == 1:

            modules.datentime1.datetime_menu()

        elif ch == 2:

            modules.mathematical.math_menu()

        elif ch == 3:

            modules.random1.random_menu()

        elif ch == 4:

            modules.uuid1.uuid_generate()

        elif ch == 5:

            modules.file1.file_menu()

        elif ch == 6:

            module = input("Enter module for attribute:")

            print("Available Attributes:",dir(module))

        elif ch == 7:

            print("Thank you for using the Multi-Utility Toolkit!")

            break
        else:

            print("Invalid Choice please choose between 1 to 7")

if __name__ == "__main__":

    main()



