class MyDate:
    pass


class MyTime:
    def __init__(self, h=0, m=0, s=0):
        self.hour = h
        self.minute = m
        self.second = s
    
    def __str__(self):
        # h = self.hour
        # m = self.minute
        # s = self.second
        # if self.hour < 10:
        #     h = f'0{self.hour}'
        # if self.minute < 10:
        #     m = f'0{self.minute}'
        # if self.second < 10:
        #     s = f'0{self.second}'
        # return f"{h}:{m}:{s}"
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"

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
    
    # def __add__(self, other):
    #     time = MyTime()
    #     time.add_seconds(self.second) 
    #     time.add_seconds(other.second)

    #     time.add_minutes(self.minute) 
    #     time.add_minutes(other.minute)

    #     time.add_hours(self.hour) 
    #     time.add_hours(other.hour)
    #     return time 

    def __add__(self, other):
        time = MyTime(self.hour, self.minute, self.second)
        time.add_seconds(other.second)
        time.add_minutes(other.minute)
        time.add_hours(other.hour)
        return time

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

time1 = MyTime(m=5, h=15, s=1)  # 15:5:1
time2 = MyTime(m=2, h=10, s=3) #10:2:3
# time1.add_time(time2)
time3 = time1 + time2
print(time3)
# 1:57:45
# print(time1 < time2)
# time1.add_hours(26)
# time1.add_minutes(65)
# time1.add_seconds(59)
# print(time1)

    