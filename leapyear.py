import sys

def leap(year: int) -> str:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return "leap year"
    else:
        return "not leap year"

if __name__ == "__main__":
    year = int(sys.argv[1])
    print(leap(year))
