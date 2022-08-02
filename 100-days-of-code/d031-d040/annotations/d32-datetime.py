import datetime as dt

now = dt.datetime.now()
print(now)          # 2022-08-02 09:46:22.609314
print(type(now))    # <class 'datetime.datetime'>

year = now.year
month = now.month
day = now.day
print(type(year),   # <class 'int'>
      type(month),  # <class 'int'>
      type(day)     # <class 'int'>
      )

day_of_week = now.weekday()

print(day_of_week)  # 0 = Monday 1 = Tuesday (...)

# Creating a datetime object:

date_of_birth = dt.datetime(year=2020, month=7, day=14)
print(date_of_birth)