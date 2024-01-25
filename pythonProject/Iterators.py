list = [1,2,3,4,5,"saif","ashik","mehedi"]
for i in list:
    print(i)

    
x = iter(list)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
