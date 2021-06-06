class Time_interval:
    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def __str__(self):
        return "{} : {} : {}".format(self.hours, self.minutes, self.seconds)
    
    def __add__(self, other):
        self.seconds = self.seconds + other.seconds
        if self.seconds > 59:
            self.minutes += 1
            self.seconds = self.seconds % 60
        self.minutes = self.minutes + other.minutes
        if self.minutes > 59:
            self.hours += 1
            self.minutes = self.minutes % 60
        self.hours += other.hours
        
        return "{} : {} : {}".format(self.hours, self.minutes, self.seconds)
    
    def __sub__(self, other):
        self.seconds = self.seconds - other.seconds
        if self.seconds < 0:
            self.minutes -= 1
            self.seconds = self.seconds % 60
        self.minutes = self.minutes - other.minutes
        if self.minutes < 0:
            self.hours -= 1
            self.minutes = self.minutes % 60
        self.hours -= other.hours
        
        return "{} : {} : {}".format(self.hours, self.minutes, self.seconds)

    def __mul__(self, integer):
        self.seconds = self.seconds * integer
        if self.seconds > 0:
            self.minutes += self.seconds // 60
            self.seconds = self.seconds % 60
        self.minutes = self.minutes * integer
        if self.minutes > 0:
            self.hours += self.minutes // 60
            self.minutes = self.minutes % 60
        self.hours *= integer

        return "{} : {} : {}".format(self.hours, self.minutes, self.seconds)

interval1 = Time_interval(24,00,00)
interval2 = Time_interval(1,30,30)

print(interval1-interval2)