from datetime import time, timedelta


class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        check = times1 = timedelta(
            hours=self.clock1.hours,
            minutes=self.clock1.minutes,
            seconds=self.clock1.seconds,
        ) - timedelta(
            hours=self.clock2.hours,
            minutes=self.clock2.minutes,
            seconds=self.clock2.seconds,
        )
        if check.total_seconds() > 0:
            times = str(check).split(":")
            difference = time(int(times[0]), int(times[1]), int(times[2])).strftime(
                "%H: %M: %S"
            )
            return difference
        else:
            return time(0, 0, 0).strftime("%H: %M: %S")

    def __len__(self):
        times1 = timedelta(
            hours=self.clock1.hours,
            minutes=self.clock1.minutes,
            seconds=self.clock1.seconds,
        ) - timedelta(
            hours=self.clock2.hours,
            minutes=self.clock2.minutes,
            seconds=self.clock2.seconds,
        )
        return int(times1.total_seconds())


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        times = (self.hours * 3600) + (self.minutes * 60) + self.seconds
        return times


dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt)  # 01: 30: 00
len_dt = len(dt)  # 5400
print(len_dt)
