#  Python Strings methods

a = "test"
print(isinstance(a,str))

# b = int(input("Enter a number : "))
# print(isinstance(b,int))

a = 11
c = str(a)
print(type(c))

data = "Hello I am Nabraj"
print(data.count("a"))
print(data.count("A"))
# search = input("Enter a character to search a char from word: ")
# print(search)
print(data.isalpha())

data1 = "11"
print(data1.isnumeric())


data2 = '''
this is multiline string
this is multiline string
this is multiline string
this is multiline string
this is multiline string
this is multiline string
'''


#______________________________
# if condition

a = input("Enter a number: ")
if a.isnumeric():
    b = int(a)
    print(b)
else:
    print("please enter a valid number")


#__________________________________

n = float(input("Enter a number: "))
if n>=80 and n<=100:
    print("Distinction")
elif n>=60 and n<=79:
    print("First Division")
else:
    print("Fail!!!")
    
    
#________________________________________

a = 50
if a%2==0:
    print('even')
else:
    print('odd')