class MyDate:
    pass


class MyTime:
    def __init__(self, h=0, m=0, s=0):
        self.hour = h
        self.minute = m
        self.second = s
    
    def __str__(self):
        return f"{self.hour}:{self.minute}:{self.second}"
    
    def add_time(self, MyTime):
        pass

    def add_seconds(self, s):
        pass

    def add_minutes(self, m):
        pass

    def add_hours(self, h):
        if self.hour + h >= 24:
            self.hour = (self.hour + h) % 24
        else:
            self.hour = self.hour + h


# 11:15:25
# 10:10:55
# 21:26:20
# 00:45:00
# 31:00:00
# 07:26:20

time1 = MyTime(m=15, h=11, s=25)
print(time1)

    