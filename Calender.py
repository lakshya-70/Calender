# 8th github project ---> Calender
import calendar
import sys
try :
    year = int(input("Enter year for which you want to generate calender"))
    month = int(input("Enter month number for which you want to generate calender"))
    if month < 1 or month > 12:
        raise ValueError

except ValueError:
    print("you entered invalid info \n please try again")
    sys.exit(1)

print(calendar.month(year ,month))