# abitary positional arguments

def test(*data):
    sum = 0
    for i in data:
        sum = sum + 1
    return sum

print(test(1,2,3,4,5))
print(test(1,2))
print(test(1,1,1,1,1,1,1,1))


# abitary keyword arguments

def test2(**data):
    print(data)
    return None

test2(name = "hello", surname="world")


def test3(a,*args,**kwargs):
    print("arguments", a)
    print("positional arguments",args)
    print("keyword arguments", kwargs)
    
test3(1,2,3,4,5, name="hello", surname="world" )




print("__________________________________________")

# Recursion  (Imp topic)

n = 10

def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*fact(n-1)
    
n = 10
print(f'factorial of {n} is {fact(n)}')



def fibo(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
print(fibo(5))



# global variable and local variable

cc = 11

def test():
    global cc
    for i in range(1,11):
        print(cc)
test()
print(cc)