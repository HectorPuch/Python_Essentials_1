year = int(input("Enter a year: "))

if year < 1582:
    print("It is not within the Gregorian calendar period.")
else:
    if year % 4 != 0:
        print("Common Year.")
    elif year % 100 != 0:
        print("Leap-year.")
    elif year % 400 != 0:
        print("Common Year.")
    else:
        print("Leap-year.")
