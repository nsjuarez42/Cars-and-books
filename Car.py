import Motor
import sqlite3

#builder pattern here
#factory for engine
class Car:

    def __init__(self,brand,model,price,cilinders =0,cv=0,hp=0):
        #default values for Car without motor
        self.on = False
        self.brand = brand
        self.price = price
        self.motor = Motor(cilinders,cv,hp)

    def turn_on(self):
        
        if not self.on:
            self.on = True
        else:
            print("Car already turned on.")

    def turn_off(self):
        if self.on:
            self.on = False
        else:
            print("")

    
    
    
        
