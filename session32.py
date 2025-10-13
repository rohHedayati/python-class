class Date:
    def __init__(self, y, m, d):
        self.year = y
        self.month = m
        self.day = d

    def __str__(self):
        return f"{self.year}/{self.month:02}/{self.day:02}"

    def __add__(self, other):
        my_date = Date(self.year, self.month, self.day)
        my_date.add_day(other.day)
        my_date.add_month(other.month)
        my_date.add_year(other.year)
        return my_date

    def add_day(self, d):
        days = self.day + d
        self.day = days % 30
        self.add_month(days//30)

    def add_month(self, m):
        months = self.month + m
        self.month = 12 if months % 12 == 0 else months % 12 
        if months % 12 == 0:
            self.add_year((months//12) - 1 )
        else:
            self.add_year(months//12)

    def add_year(self, y):
        self.year += y

class Time:
    def __init__(self, h=0, m=0, s=0):
        self.hour = h
        self.minute = m
        self.second = s
    
    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"

    def __lt__(self, other):
        return (self.hour, self.minute, self.second) < (other.hour, other.minute, other.second)

    def __add__(self, other):
        time = Time(self.hour, self.minute, self.second)
        time.add_seconds(other.second)
        time.add_minutes(other.minute)
        time.add_hours(other.hour)
        return time

    def add_seconds(self, s):
        new_s = self.second + s
        if new_s >= 60:
            self.second = new_s % 60
            self.add_minutes(new_s // 60)
        else:
            self.second = new_s

    def add_minutes(self, m):
        new_m = self.minute + m
        if new_m >= 60:
            self.minute = new_m % 60
            self.add_hours(new_m // 60)
        else:
            self.minute = new_m

    def add_hours(self, h):
        if self.hour + h >= 24:
            self.hour = (self.hour + h) % 24
        else:
            self.hour = self.hour + h

class DateTime(Date,Time):
    def __init__(self, y, m, d, h,mi, s):
        Date.__init__(y,m,d)
        Time.__init__(h,mi,s)




date1 = Date(1404,7,21)
date2 = Date(1404,5,1)
# date.add_month(25)
# date.add_day(200)
# print(date)
print(date1 + date2)


x = 10
if x % 2 == 0:
    print("even")
else:
    print("odd")

msg = "even" if x%2==0 else "odd"
print(msg)