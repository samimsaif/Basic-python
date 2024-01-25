 # Constractor

#  class employees:
#      def saifsFamily(self,name,age):
#          print(f"my name is {name}, my age is {age}")
#
# p1 = employees()
# p1.saifsFamily("saif", 25)

# class parentInfo:
#
#     def saifsFamily(self,name,age):
#         print(f"my name is {name}, my age is {age}")
#
# p1 = parentInfo()
# p1.saifsFamily("saif", 25)
# p1.saifsFamily("mukul", 29)
# p1.saifsFamily("farha", 33)
# p1.saifsFamily("ruby", 37)

# class parentInfo:
#     def __init__(self,name, number):
#         print(f"my name is {name}, my number is {number}")
#
# p1 = parentInfo("saif", "01648147680")

# class className:
#     def instantmethod(self):
#         print(" hello world ")
#
#     @classmethod
#     def Classmethod(cls):
#         print(" this is class method")
#
#     @staticmethod
#     def staticMethod():
#         print("this is staticmethod")
#
# a1 = className()
# a1.instantmethod()
# a1.Classmethod()
# className.staticMethod()

#  Polymorphism

class Vehicle:
    def __init__(self, Model, Brand, Component):
        self.Model = Model
        self.Brand = Brand
        self.Component = Component

class Plane(Vehicle):
    pass

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

a1 = Plane("M27", "Porcha","All Component")
print(a1.Brand)
print(a1.Model)
print(a1.Component)

c1 = Plane("R15", "Honda","Main Component")
print(c1.Component,c1.Brand,c1.Model)

c1 = Plane("Gixxer SF 150 FI ABS", "Suzuki","Component")
print(c1.Brand)
print(c1.Model)
print(c1.Component)
