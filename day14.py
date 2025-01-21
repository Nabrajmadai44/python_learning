# Except Handling

'''
try:
    code block
except:
    error handling
'''
# a = 10
# try:
#     print(b) # print(a/0)
# except NameError as e:
#     print(e)
# except ZeroDivisionError as e:
#     print(e)
# except:
#     print("Something went wrong")
    
    
def sum():
    a = 4
    b = 2
    try:
        print(a+b)
    except:
        print("Something went wrong")
print(sum())
print()