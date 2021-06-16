def LipYear(y):
    if ((y % 400 == 0) or
            (y % 100 != 0) and
            (y % 4 == 0)):
        return "its a leap year";
    else:
        return "its not a leap year";
# Driver code
if __name__ == '__main__':
    year = int(input("Enter a year: "));
    print(LipYear(year));
'''
[10: 49AM] TejasChokshi

year = int(input("Enter a year: "))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
'''
