import sys
def leap(year):
    if (year%4 ==0):
        print("Is a leap year")
    else:
        print("Not a leap year")

        year =int(sys.argv[1])
        leap(year)