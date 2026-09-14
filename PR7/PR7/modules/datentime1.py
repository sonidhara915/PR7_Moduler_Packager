from datetime import datetime
import time

def current_datetime():

    now = datetime.now()

    print("Current date and time is:",now)


def diffrent_datetime():

    try:
        start_date = input("Enter your start date(YYYY-MM-DD):")
        end_date = input("Enter your end date(YYYY-MM-DD):")

        date1 = datetime.strptime(start_date,"%y-%m-%d")
        date2 = datetime.strptime(end_date,"%y-%m-%d")

        diffrent = abs((date2-date1).days)

        print("The days different between two dates:",diffrent)
    except ValueError:
        print("Invalid date enter please try again")


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

     try:
          second = int(input("Enter couuntdown seconds:"))

          assert second > 0 ,"Enter only positive number."

          for i in range (second,0,-1):

               print("Time Left:",i,"seconds")

               print("Time 's up!")
               
               time.sleep(1)

               

     except ValueError:
          
          print("Invalid input.")

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