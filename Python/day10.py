# class and object

'''
syntax eg

class Car():
    wheel = 4
    
    def move:
        pass
    def stop:
        pass
    constructor
    
obj = Car()
'''

class Test():
    a = 10
    b = 20
obj = Test()
obj1 = Test()

print(obj.a)
print(obj1.b)
print(obj1.b == obj.a)
# obj1.b = 15
# del obj1
# print(obj1.b)


class Test2():
    a = 100
    
    def add(sudan):
        print(sudan.a)
    
obj = Test2()
obj.add()

print("_____________")

class Math():
    a = 2
    b = 4   
    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a- self.b
    
    def mult(self):
        return self.add() *self.b
    
obj = Math()
print(obj.add())
print(obj.sub())
print(obj.mult())




# Constructor   (imp topic)

class Testing():
    def __init__(self):
        print("This is constructor")
        return None
    
obj = Testing()
print(obj)
