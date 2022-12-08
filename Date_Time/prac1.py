# Exercise 1: Print current date and time in Python
import datetime

# Print date and time
print(datetime.datetime.now())

# only time
print(datetime.datetime.now().time())

# Solution 2 using time.strftime()
# from time import gmtime, strftime
# print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))



# Exercise 2: Convert string into a datetime object
# For example, You received the following date in string format. Please convert it into Python’s DateTime object.
# Given:
# date_string = "Feb 25 2020 4:20PM"
# Expected output:
# 2020-02-25 16:20:00

from datetime import datetime
date_string = "Feb 25 2020  4:20PM"
datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print(datetime_object)



# Exercise 3: Subtract a week (7 days)  from a given date in Python
# given_date = datetime(2020, 2, 25)
# Expected output:
# 2020-02-18

from datetime import datetime, timedelta

given_date = datetime(2020, 2, 25)
print("Given date")
print(given_date)

days_to_subtract = 7
res_date = given_date - timedelta(days=days_to_subtract)
print("New Date")
print(res_date)



# Exercise 4: Print a date in a the following format
# Day_name  Day_number  Month_name  Year

# Given:
# given_date = datetime(2020, 2, 25)
# Expected output:
# Tuesday 25 February 2020

from datetime import datetime

given_date = datetime(2020, 2, 25)
print("Given date is")
print(given_date.strftime('%A %d %B %Y'))



# Exercise 5: Find the day of the week of a given date
# Given:
# given_date = datetime(2020, 7, 26)
# Expected output:
# Sunday

from datetime import datetime

given_date = datetime(2020, 7, 26)

# to get weekday as integer
print(given_date.today().weekday())

# To get the english name of the weekday
print(given_date.strftime('%A'))

