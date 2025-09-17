class Math():
    
    def __init__(self, n, bm):
        self.a = n
        self.b = bm
        ...
        
    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a- self.b
    
    def mult(self):
        return self.a *self.b
    
    
obj = Math(5, 4)
print(obj.add())
print(obj.sub())
print(obj.mult())



class Math2():

    def __init__(self,*data):
        self.data = data
        self.sum = 0

    def add(self):
        for i in self.data:
            self.sum = self.sum+i
        return self.sum


obj= Math2(5,1,4,2,2,2,2,2)
obj1= Math2(5,1,4,2,55,6,5,6,6,2,2,2)
obj2= Math2(5,1,4,2,55,6,2,2)


print(obj.add())
print(obj1.add())
print(obj2.add())


print("==========================")


class Parent():
    a = 2
    b = 3

class Child(Parent):
    c = 5
    a = 53 
obj = Child()
print(obj.a)
print(obj.b)
print(obj.c)


print("=========================>")
 
class Parent():
    def __init__(self,name,age):
        self.name = name
        self.age = age
   
class Child(Parent):
    def printName(self):
        return f"Hello, My name is: {self.name} and I'm {self.age} years old"
 
obj = Child("Nabraj", 22)
print(obj.printName())


print("=========================")

class Parent():
    def __init__(self,name,age):
        self.name = name
        self.age = age
       
    def printName(self):
        return f"Hello, my name is: {self.name}"
   
class Child(Parent):
   
    def __init__(self,name,age):
        self.name = "Nabu"
        super().__init__(name, age)
       
       
obj = Child("Nabraj", 22)
print(obj.printName())



class Parent():
    def __init__(self):
        self.test = "This is world"
        
class Child(Parent):
    def __init__(self):
        self.a = 33
        self.t = "hello"
        Parent.__init__(self)
        
    def testing(self):
        return self.t, self.t
    
obj = Child()
print(obj.testing())