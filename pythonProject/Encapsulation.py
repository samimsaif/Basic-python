# capsulation
# class Parent:
#     def __init__(self, Name, FatherName):
#         self.Name = Name
#         self.FatherName = FatherName
#
# p1 = Parent("Saif Uddin Ahmed", "Salah Uddin Ahmed")
# print(p1.FatherName)

# Encapsulation

class Parent:
    def __init__(self, Name, FatherName):
        self.__Name = Name
        self.FatherName = FatherName
        print(self.__Name)

p1 = Parent("Saif Uddin Ahmed", "Salah Uddin Ahmed")
print(p1.__Name)