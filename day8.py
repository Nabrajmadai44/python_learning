# function

def message():
    print("I am learning function")
    
print(message())


'''
Positional arguments
Keyword arguments
default arguments
arbitary positional arguments
arbitary keyword arguments
'''


# Positional arguments

def family(father, mother):
    return father, mother

print(family("Bhana", "Bhim"))


def sum_mul(a,b):
    result = a +b, a*b
    return result
print(sum_mul(10,20))
    
def simpleinterst(p, t, r):
    result = (p*t*r)/100
    return result
p = 10
t = 5
r = 5
data = simpleinterst(p, t, r)
print(data)

def user_info(first, last="Madai"):
    return first, last
print(user_info("Nabraj"))
print(user_info("Nabraj", "xettri"))