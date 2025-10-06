import datetime
import jdatetime

# d = datetime.date(2025, 10, 8)
# print(d.weekday())
# print(datetime.time(10, 30))

jdate = jdatetime.datetime.now()
print(jdate)
format_date = jdate.strftime("%a, %d %b %Y %H:%M:%S")
print(format_date)