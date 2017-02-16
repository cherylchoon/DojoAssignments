class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayinfo(self):
        print self.price
        print self.max_speed
        print self.miles
        return self

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        if self.miles >=5:
            self.miles -= 5
        return self

bike1 = Bike('200', '25mph')
bike2 = Bike('150', '20mph')
bike3 = Bike('300', '30mph')

for _ in range(3):
    bike1.ride()
bike1.reverse().displayinfo()

for _ in range(2):
    bike2.reverse()
bike2.displayinfo()

for _ in range(3):
    bike3.reverse()
bike3.displayinfo()
