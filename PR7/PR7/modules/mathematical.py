import math
from modules.Shapes import rectangle
from modules.Shapes import circle

def factorial_num():

    try:

        num = int(input("Emter a number for fectorial:"))

        fectorial = math.factorial(num)

        print("Factorial :",fectorial)

    except ValueError:

        print("Invalid Input")

def compound_interest():

    try:

        p = float(input("Enter Principal amount:"))

        r = float(input("Enter rate of interest(in %):"))

        t = float(input("Enter time (in years):"))

        amount = p*(1+r/100)**t

        i = amount - p

        print("compound intrest:",round(i,2))

        print("Total Amount:",round(amount,2))

    except ValueError:

        print("Invalid input!")


def trigonometric():

    try:

        angle = float(input("Enter angle in degrees:"))

        radians = math.radians(angle)

        print("sin:",round(math.sin(radians),4))
        print("cos:",round(math.cos(radians),4))
        print("tan:",round(math.tan(radians),4))

    except ValueError:

        print("Invalid input")

def area_shapes():

    print("\n Area of Geometric Shapes:")
    print("1.Circle.")
    print("2.Rectangle")

    choice = int(input("enter your choice:"))

    if choice == 1:

        r = float(input("Enter a redious of circle:"))
        print(circle.area(r))

    elif choice == 2:

        l = float(input("Enter a lenght:"))
        w = float(input("Enter a width:"))

        print(rectangle.area_rec(l,w))

    else:

        print("Invalid Choice")



def math_menu():

    while True:

        print("\nMathematical Operations:")
        print("1.Calculate Fectorial")
        print("2.Solve Compound Intrest")
        print("3.Trgonometric Calculations")
        print("4.Area of Geometric Shapes")
        print("5.Back to Main Menu")

        ch = int(input("Enter your choice:"))

        if ch == 1:

            factorial_num()

        elif ch == 2:

            compound_interest()

        elif ch == 3:

            trigonometric()

        elif ch == 4:

            area_shapes()

        elif ch == 5:
            
                break
        else:

            print("Invalid choice")









