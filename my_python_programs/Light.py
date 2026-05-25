class Light:
    def __init__(self,light_is="OFF"):
        self.light_is=light_is
    
    def turn_on(self):
        if self.light_is == "OFF":
            self.light_is = "ON"
        else:
            print("Light is already ON")
    
    def turn_off(self):
        if self.light_is == "ON":
            self.light_is = "OFF"
        else:
            print("Light is already OFF")
    
    def status(self):
        return self.light_is 
        
l=Light()
print(l.status())
l.turn_on()
print(l.status())
l.turn_off()
print(l.status())
l.turn_off()
print(l.status())
l.turn_on()
print(l.status())
l.turn_on()