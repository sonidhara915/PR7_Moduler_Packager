import random
import string

def random_num():

    try:

        s = int(input("Enter minimum num:"))

        e = int(input("Enter maximum num:"))

        if s > e:
            print("Minimum can not be greater than maximum")

            return
        print("Random Number:",random.randint(s,e))

    except ValueError:

        print("Invalid Input")

def random_list():

    try:

        s = int(input("Enter list size:"))

        S = int(input("Enter minimum num:"))

        e = int(input("Enter maximum num:"))

        assert s < 0 or S > e,"Invalid range for size"

        number = [random.randint(S.e) for _ in range(s)]

        print("Rendom List:",number)

    except ValueError:

        print("Invalid Value") 

def password():

    try:

            l = int(input("Enter password length:"))

            c = string.ascii_letters+string.digits+string.punctuation

            p = ''.join(random.choice(c) for i in range(l))

            print("Random Password:",p)

    except ValueError:

        print("Invalid Input")

def otp():

    otp = random.randint(100000,999999)

    print("Your OTP is:",otp)


def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            random_num()
        elif choice == "2":
            random_list()
        elif choice == "3":
            password()
        elif choice == "4":
            otp()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")