class Time_interval:
    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def __str__(self):
        return "{} : {} : {}".format(self.hours, self.minutes, self.seconds)
    
    def __add__(self, other):
        try:
            if isinstance(other,int):
                self.seconds = self.seconds + other
            else:
                self.seconds = self.seconds + other.seconds
            if self.seconds > 59:
                self.minutes = self.seconds // 60
                self.seconds = self.seconds % 60
            if isinstance(other,Time_interval):
                self.minutes = self.minutes + other.minutes
            if self.minutes > 59:
                self.hours += 1
                self.minutes = self.minutes % 60
            if isinstance(other,Time_interval):
                self.hours += other.hours
                
            return "{} : {} : {}".format(self.hours, self.minutes, self.seconds)
        except:
            return "Need timeinterval object to add"
    
    def __sub__(self, other):
        try:            
            if isinstance(other,int):
                self.seconds -= other
            else:
                self.seconds = self.seconds - other.seconds
            if self.seconds < 0:
                self.minutes = self.seconds // 60
                self.seconds = self.seconds % 60
            if isinstance(other, Time_interval):
                self.minutes = self.minutes - other.minutes
            if self.minutes < 0:
                self.hours -= 1
                self.minutes = self.minutes % 60
            if isinstance(other, Time_interval):
                self.hours -= other.hours
            
            return "{} : {} : {}".format(self.hours, self.minutes, self.seconds)
        except:
            return "Need timeinterval object to add"

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

if __name__ == "__main__":
    interval1 = Time_interval(24,00,00)
    interval2 = Time_interval(1,30,30)
    print("interval1 =",interval1,", interval2 =", interval2)
    print(interval1 + interval2)
    print(interval1 + 200)
    print(interval1 - 30)
    print(interval1 - interval2)
    print(interval1 * 2)
