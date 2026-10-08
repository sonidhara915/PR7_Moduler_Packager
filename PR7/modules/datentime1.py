from datetime import datetime
import time

def current_datetime():

    now = datetime.now()

    print("Current date and time is:",now)


def diffrent_datetime():

    data1 = input("Enter first date (YYYY-MM-DD): ")
    data2 = input("Enter second date (YYYY-MM-DD): ")

    try:

        date1 = datetime.datetime.strptime(
            data1, "%Y-%m-%d"
        ).date()

        date2 = datetime.datetime.strptime(
            data2, "%Y-%m-%d"
        ).date()

        difference = abs((date2 - date1).days)

        print("Difference:", difference, "days")

    except ValueError:

        print("Invalid date format. Use YYYY-MM-DD.")


def formate_datetime():

    try:

        date = input("Enter your date(YYYY-MM-DD):")

        Date = datetime.strptime(date,"%y-%m-%d")

        print("Formate date:",Date.strftime("%d-%m-%y"))

    except ValueError:

        print("invalid date formate")

def stopwatch():

        input("Enter for start stopwatch:")

        start_time = time.time()

        input("Enter for stop stopwatch:")

        end_time = time.time()

        time_gap = end_time - start_time

        print("Total Time:",round(time_gap,2),"seconds")


def countdown_timer():

    ch1 = int(input("Enter countdown seconds: "))

    print("\nCountdown started...")

    while ch1 > 0:

        print(ch1)

        time.sleep(1)

        ch1 -= 1

    print("Time's up!")

def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            current_datetime()
        elif choice == "2":
            diffrent_datetime()
        elif choice == "3":
            formate_datetime()
        elif choice == "4":
            stopwatch()
        elif choice == "5":
            countdown_timer()
        elif choice == "6":
            break
        else:
            print("Invalid choice!")