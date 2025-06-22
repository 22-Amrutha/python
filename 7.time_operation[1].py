print("name:amrutha;usn:1AY24AI007;SECTION:M")

class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def to_seconds(self):
        return self.h * 3600 + self.m * 60 + self.s

    def from_seconds(self, total):
        h = total // 3600
        m = (total % 3600) // 60
        s = total % 60
        return Time(h, m, s)

    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"

def mul_time(time, number):
    total = time.to_seconds() * number
    return time.from_seconds(int(total))

def average_pace(finishing_time, distance):
    return mul_time(finishing_time, 1 / distance)

# Example
t = Time(1, 10, 0)   # 1 hr 10 min
pace = average_pace(t, 10)
print("Average pace per mile/km:",pace)
