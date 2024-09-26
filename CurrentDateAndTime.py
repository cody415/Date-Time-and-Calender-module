from datetime import date,time,datetime

# calling the today
# function of date class
today=date.today()
now=datetime.now()
print("Todays date is", today)
print("\n current date and time is", now)

# printing date's componebts
print("\n date component",today.year,today.month,today.day)
