class Rectangle:
    def __init__(self, __length, width):
        self.__length=__length
        self.width=width
    
    def get_data(self):
        return self.__length
        
    def area(self):
        return self.__length * self.width
    
    def perimater(self):
        return 2*(self.__length + self.width)
        
c = Rectangle(10,20)
#print(a.__length)    ---- will throw Error
print(f"Private Attribute Lenght value is : {c.get_data()}")
print(f"Area of Rectangle is {c.area()}")
print(f"Perimeter of Rectangle is {c.perimater()}")