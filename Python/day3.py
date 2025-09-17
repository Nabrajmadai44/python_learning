# Nested if condition
age = 30
memeber  = True
if age > 18:
    if memeber:
        print("The ticket price is $12")
    else:
        print("The ticket price is $16")
else:
    if memeber:
        print("The ticket price is $8")
    else:
        print("The ticket price is $11")
    




# Iteration

# for loop

'''
Syntax
for i in "Nabraj"\
    print(i)
'''
for i in "Python":
    print(i)
    
a = "Coder"
print(a[0])

# print(a[10])   index error out of range

for i in range(0,50,1):
    print(i)
'''
0 = > start value
50 => end value
1 => step value
'''


for i in range(2,21,2):
    print(i)
    

# break

for i in range(1,11,1):
    if i == 5:
        break
    print(i)
    
# continue

for i in range(1,11,1):
    if i == 5:
        continue
    print(i)


#_____________________
Data = "Hello"
for i in range(0,len(Data)):
    print(Data[i])


# string formatting or f string
for i in range(1,11,1):
    a = f'2 X {i} = {2*i}'  # multiple of 2
    print(a)

#nested for loop_____
for i in range(1,3):
    for a in range(1,4):
        print(i,a)   
        


# Number pattern       

for i in range(1,6):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()
    
for i in range(10,1,-1):
    print(i)



# while loop__________________

   






