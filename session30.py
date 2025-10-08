class MyDate:
    pass


class MyTime:
    def __init__(self, h=0, m=0, s=0):
        self.hour = h
        self.minute = m
        self.second = s
    
    def __str__(self):
        return f"{self.hour}:{self.minute}:{self.second}"
    
    def __lt__(self, other):
        # if self.hour < other.hour:
        #     return True
        # elif self.hour == other.hour:
        #     if self.minute < other.minute:
        #         return True
        #     elif self.minute == other.minute:
        #         if self.second < other.second:
        #             return True
        # return False
        return (self.hour, self.minute, self.second) < (other.hour, other.minute, other.second)
    
    def __add__(self, other):
        pass

    def add_time(self, other):
        pass

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
            # self.hour += new_m // 60
            self.add_hours(new_m // 60)
        else:
            self.minute = new_m

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

time1 = MyTime(m=15, h=10, s=20)
time2 = MyTime(m=15, h=10, s=25)
# time1.add_time(time2)
time1 + time2
print(time1 < time2)
# time1.add_hours(26)
# time1.add_minutes(65)
# time1.add_seconds(59)
# print(time1)

    