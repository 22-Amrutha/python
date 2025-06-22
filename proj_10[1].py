print("name:amrutha;usn:1AY24AI007;SECTION:M")

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.seconds = hour * 3600 + minute * 60 + second

    def __str__(self):
        h = self.seconds // 3600
        m = (self.seconds % 3600) // 60
        s = self.seconds % 60
        return f"{h:02d}:{m:02d}:{s:02d}"

    def time_to_int(self):
        return self.seconds

    def increment(self, seconds):
        return Time(0, 0, self.seconds + seconds)

    def is_after(self, other):
        return self.seconds > other.seconds


def int_to_time(seconds):
    return Time(0, 0, seconds)

start = Time(9, 45, 0)
print("Start:", start)

duration = Time(1, 35, 0)
print("Duration:", duration)

done = start.increment(duration.time_to_int())
print("Done:", done)

print("Is done after start?", done.is_after(start))
