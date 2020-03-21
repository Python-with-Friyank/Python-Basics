# Class
class Point:
    # Constructor
    def __init__(self,X,Y):
        self.x = X
        self.y = Y
    # MEthods of Class

    def move(self):
        print(f"Move {self.x} , {self.y}")
    # Method of Class

    def Draw(self):
        print(f"Draw {self.x}  {self.y}")


pointObj = Point(11,22)
pointObj.move()

