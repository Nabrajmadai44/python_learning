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



'''
BaseException : The base class for all built-in exceptions.
Exception	: The base class for all non-exit exceptions.
ArithmeticError : Base class for all errors related to arithmetic operations.
ZeroDivisionError :	Raised when a division or modulo operation is performed with zero as the divisor.
OverflowError :	Raised when a numerical operation exceeds the maximum limit of a data type.
FloatingPointError :	Raised when a floating-point operation fails.
AssertionError	: Raised when an assert statement fails.
AttributeError	: Raised when an attribute reference or assignment fails.
IndexError	: Raised when a sequence subscript is out of range.
KeyError	: Raised when a dictionary key is not found.
MemoryError	: Raised when an operation runs out of memory.
NameError	: Raised when a local or global name is not found.
OSError	Raised : when a system-related operation (like file I/O) fails.
TypeError	: Raised when an operation or function is applied to an object of inappropriate type.
ValueError	: Raised when a function receives an argument of the right type but inappropriate value.
ImportError	: Raised when an import statement has issues.
ModuleNotFoundError	: Raised when a module cannot be found.
'''


# file handling

##exception handling
# try:
#     f = open("day.py", 'r')
#     print(f.read())
# except FileNotFoundError as e:
#     print("file doesot found")
    