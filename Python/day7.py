# tuple 

# Note : In case of list, we use square
# brackets []. Here we use round brackets ()
t = (10, 20, 30) 

print(t)
print(type(t))


'''Unlike Python lists, tuples are immutable. Some Characteristics of Tuples in Python.

Like Lists, tuples are ordered and we can access their elements using their index values
We cannot update items to a tuple once it is created. 
Tuples cannot be appended or extended.
We cannot remove items from a tuple once it is created. '''

t = (1, 2, 3, 4, 5)

# tuples are indexed
print(t[1])
print(t[4])

# tuples contain duplicate elements
t = (1, 2, 3, 4, 2, 3)
print(t)

# updating an element
t[1] = 100
print(t)





# set

a = { 1,2,3,"hello",3,34,12324,"hlo"}
print(a)
print(type(a))


c = list(a)
print(type(c))
c.append("4444")
print(c)

b = set(c)
print(type(b))
print(b)




# list comprehension

a = []
for i in range(1,10,1):
    a.append(i)
print(a)


bb = [i for i in range(1,20,1)]
print(bb)


'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''