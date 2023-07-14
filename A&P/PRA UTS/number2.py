import calendar

# get year and month from user input
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

# create calendar for given year and month
cal = calendar.monthcalendar(year, month)

# print calendar
print(calendar.month_name[month], year)
print("Mo Tu We Th Fr Sa Su")
for week in cal:
    for day in week:
        if day == 0:
            print("  ", end="")
        else:
            print("{:2d}".format(day), end=" ")
    print()
