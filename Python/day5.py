# in-built datatypes
# 1. list
# 2. dictionary
# 3. set
# 4. tuple

# list and dictionary are mutuable datatypes
# set and tuple are immutable datatypes


# list

a = [1,2,3,4,5,6]
print(a[4])
print(type(a))

b = [1, "2", "hello", 3.3, True]
print(b[2])
print("negative index", b[-2])

# len of list
print(len(b))


for i in range(len(b)):
    print(b[i])
    


## list methods

# slicing
print(b[1:3])
print(b[:])
print(b[:4])
print(b[2:])


# append

c = [1,2,3,4,5]
c.append(6)
print(c)


data = [1,2,3,4,5, ["hello", "namaste"]]
print(data[5][1])


    
# list_data = []
# for i in range(5):
#     j = input("Enter a data: ")
#     list_data.append(j)
# print(list_data)



# Insert

a = ["hello", "world", "testing", "something"]
a.insert(1, "Nabraj")
a.insert(1, "coder")
a.insert(4, "test")
print(a)


# extends
a = ["hello", "world", "testing", "something"]
b = [1,2,3,4]
# b.extend(a)
print(b)

print("___________________________")
# concat
c= a+b
print("concat", c)
print(c*3)

print("___________________________")


## Deleting items/elements from existing list

# 5. del

a = ["hello", "world", "testing", "something"]
del a[3]
print(a)


# 6. remove

a = [1,2,3,4,5,5,5,6]
a.remove(5)
print(a)

# 7. pop

a = ["hello", "world", "testing", "something"]
a.pop()
a.pop()
print(a)


# 8. clear

a = ["hello", "world", "testing", "something"]
a.clear()
print(a)


## other methods

# 9.count

a = ["hello", "world", "world", "testing", "something"]
index_a = a.count("world")
print(index_a)