"""
#
# Part: Python Class abd Object
#
"""
# Build Class
class MyClass:
    x = 5
    
# Call Class
object1 = MyClass()
print ("Object1", object1.x)
object2 = MyClass()
print ("Object2", object2.x)

class SpyXFamily:
    def _init_(self, name_f, age_f): #_init_= ค่าเริ่มต้น
        self.name = name_f
        self.age = age_f
    
    def _str_(self):
        # return self.name + " - " + self.age
        return f"{self.name} - {self.age}" # จัดตัวอักษรแบบใหม่
    
    def sayHi(self, last_name = "forger"):
        print (f"Hey bruh what'sup {self.name} {last_name}")
        
p1 = SpyXFamily("Anya", 8)
print (p1.name , p1.age)
print (p1)
p1.sayHi()

p2 = SpyXFamily("Damian", 8)
print (p2.name , p2.age)
print (p2)
p2.sayHi("Desmond")
        
class Car:
    def __init__(self, body_color, engine_size):
        self.body_wheel = 4
        self.window = 4
        self.window_fornt = 1
        self.window_back = 1
        self.body_color = body_color
        self.engine_size = engine_size
        
    def push_window_button(self):
        # do someting ทำอะไร
        pass
    
    def pop_window_button(self):
        # do someting ทำอะไร
        pass
    
    def calSpeed(self):
        # speed = self.engine.size * 100
        # return speed
        return self.engine_size * 1000
    
    def turnOnfrontLight(self, status = "off"):
        if status == "on":
            # do some ting
            pass
        else:
            # do someting
            pass
        
        
        