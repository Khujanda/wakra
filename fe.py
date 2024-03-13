clss Car:
  def ____(e, br2, ml):
    self.n = b
roo
    self.mP = me

  def mve(self):
    print("D!")

class Boat:
  def __init__(self, model):
    self.brnd3 = br
    self.modl = mod

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()
