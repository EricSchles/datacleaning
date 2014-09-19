class Car:
    def __init__(self,number_of_doors=4,color="red",top_speed=140):
        self.number_of_doors= number_of_doors
        self.color = color
        self.top_speed = top_speed
        self.direction = "straight"
        
    def change_direction(self,direction):
        if not isinstance(direction,""):
            raise AssertionError("Expected type string for direction")
        if direction in ["straight","left","right","reverse"]:
            self.direction = direction
            return True
        else:
            print "Can't go that way"
            return False
    def change_speed(self,speed):
        if not isinstance(speed,0):
            raise AssertionError("expected an integer")
        if speed > 0:
            self.speed = speed
            return True
        else:
            print "You can't go less than 0 miles an hour"
            return False

class Jeep(Car):
    def __init__(self,number_of_doors=4,color="red",top_speed=170,off_road=False):
        self.number_of_doors= number_of_doors
        self.color = color
        self.top_speed = top_speed
        self.direction = "straight"

class SportsCar(Car):
    def __init__(self,number_of_doors=4,color="red",top_speed=250,off_road=False):
        self.number_of_doors= number_of_doors
        self.color = color
        self.top_speed = top_speed
        self.direction = "straight"
