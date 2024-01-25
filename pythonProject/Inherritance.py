# Inheritance
class baba:
    car = "Mustang"
    cat = "tony"
    tk = " 100 core"
class kaka(baba):
    phone = ""
    laptop = ""
k = kaka()
print(k.car)
print(k.cat)
print(k.tk)

# Multiple Inheritance
class baba:
    car = "Mustang"
    cat = "tony"
    tk = " 100 core"

class baba2:
    home = " 10 flat"
    land = " 10 katha "
    lot = "11"

class baba3:
    ac = " walton"
    micro = " havit "
    camera = "nikon"
class kaka(baba,baba2,baba3):
    phone = ""
    laptop = ""
k = kaka()
print(k.car)
print(k.camera)
print(k.land)
print(k.ac)

# MultiLevel Inheritance
class baba:
    car = "Mustang"
    cat = "tony"
    tk = " 100 core"

class son1(baba):
    home = " 10 flat"
    land = " 10 katha "
    lot = "11"

class son2(son1):
    ac = " walton"
    micro = " havit "
    camera = "nikon"
class son3(son2):
    phone = ""
    laptop = ""
k = kaka()
print(k.car)
print(k.camera)
print(k.land)
print(k.ac)