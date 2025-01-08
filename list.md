## List

- lists are ordered collection of data items 
- they store multiple items in a single variable
- list items are separated by commas and enclosed within square brackets [].
- list are changeable meaning we can alter then after creation 

### Example 1
``` python 
lst1 = [1,2,2,3,5,4,6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)

# output 
[1, 2, 2, 3, 5, 4, 6]
['Red', 'Green', 'Blue']
```

### List Length
```python
# To determine how many items a list has, use the len() function
print(len(students))
9 
```

### List Items
```python 
# Creating a list of teachers to show list allow duplicate value and list elements are ordered
teachers = ["Nasir", "Irfan", "Haris", "Sheraz", "Farhan", "Rafiq",
"Haris", "Ihsan"]
print(teachers)
['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Rafiq', 'Haris','Ihsan']

```
### List Items - Data Types
List items can be any data types
``` python
# Creating a list of string

list1 = ["Apple", "Banana", "Cherry", "Orang"]

# Creating a list of integers

list2 = [1, 4, 7, 3, 6, 0, 12, 23]

# Creating a list of boolean data type

list3 = [True, False, True, True, False]

# Craeting a list of float data type

list4 = [17.3, 71.3, 34.5, 87.0, 23.4]

```
A list can contain different data types
```python 
# Creating a list with string, integers and boolean and float data type
list5 = ["apple", 54, 71.3, False, "Orange", True, 21, 13.8]
```

### Access List Elements
List items are indexed, the positive list index start from [ 0 ] and the negative list index start from
[ -1 ], the index [ -1 ] represent the last element of the list. List elements/items access using
indexes

``` python 
# Creating a list of teachers
teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris', 'Ihsan']

print(teachers)

['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris','Ihsan']

# Access with positive indexes
print(teachers[3]) # return the number 4 element of the list

Sheraz

# Access with negative indexes
print(teachers[-1]) # return the last element of the list
Ihsan
```

### Slicing
It is possible to access a section of items from the list using the slicing operator :, not just a
single item

#### Slicing With Positive Indexes
``` python 
# Creating a list of teachers
teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris', 'Ihsan']
print(teachers)
['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris', 'Ihsan']
# Slicing with positive indexes

print(teachers[3:8]) # return the elements from index 3 to index 7, 8 not included
['Sheraz', 'Farhan', 'Khalil', 'Haris', 'Ihsan']

print(teachers[2:8:1]) # inclde every element in this range
print(teachers[2:8:2]) # include every second element in this range
['Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris', 'Ihsan']
['Haris', 'Farhan', 'Haris']

# by leaving out the start index, the range will start from first item and go on to the specific value
print(teachers[:9])
['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris', 'Ihsan']
# By leaving out the end index, the range will start from spacific value and go on to the end of the list
print(teachers[3:])
['Sheraz', 'Farhan', 'Khalil', 'Haris', 'Ihsan']
```

#### Slicing With Negative Indexes 
``` python 
# Creating a list of teachers
teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil','Haris', 'Ihsan']
print(teachers)
['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris','Ihsan']
# slicing with negative indexes
print(teachers[-7:-2]) # The range starts from the element number 2 [-7] to the element number 6 [-3], [-2] not include
['Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil']
print(teachers[:-2]) # the rang start from the first element of the list to the element number 6 [-3], [-2] not include
['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil']
print(teachers[-7:]) # the rang start from the element number 2 [-7] of the list to the end of the list
['Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris', 'Ihsan']
```


## List Metods :
Adding items/elements into an existing

### 1. Append
``` python 
# The append() add an element/item at the end of existing list
teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil',
'Haris', 'Ihsan']
teachers.append('Tariq')
print(teachers)
['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil','Haris','Ihsan', 'Tariq']
```

### 2. Insert
``` python
# The insert() method add the elemnent at the spacified position
teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil',
'Haris', 'Ihsan']
teachers.insert(4, 'Idrees')
print(teachers)
['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Idrees', 'Farhan', 'Khalil',
'Haris', 'Ihsan'] 
```

### 3. Extend
``` python 
# The extend() method adds the specified list elements (or any iterable(list, set, tuple)) to the end of the current list

teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil',
'Haris', 'Ihsan']
teachers.extend(['Idrees', 'Tariq'])
print(teachers)
['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris', 'Ihsan', 'Idrees', 'Tariq']
```

### 4.Concatenate

``` python 
# Concatenate the two lists
teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris', 'Ihsan']
students = ["Ali", "Ahmad", "Imarn", "Babar", "Haris", "Gohar", "Johar", "Rizwan", "Sami"]

# The '+' sign is used to cancatenate the lists teachers_students = teachers + students

print(teachers_students)
['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris', 'Ihsan', 'Ali', 'Ahmad', 'Imarn', 'Babar', 'Haris', 'Gohar', 'Johar', 'Rizwan', 'Sami']

```

## Deleting items/elements from existing list

### 5. Del

``` python 
# The del used to delet element of the list via index
teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil','Haris', 'Ihsan']
del teachers[4]
print(teachers)
['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Khalil', 'Haris', 'Ihsan']
```

### 6. Remove
``` python 
# The remove() method remove the element/item with the specified value(itemname)
teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris', 'Ihsan']
teachers.remove('Haris')
print(teachers)
['Nasir', 'Irfan', 'Sheraz', 'Farhan', 'Khalil', 'Haris', 'Ihsan']
```

### 7. Pop
``` python 
# The pop() method deletes the element/item from last of the list by default
teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil',
'Haris', 'Ihsan']
teachers.pop() # it return deleted element/item
'Ihsan'
# Pop element/item at the spacific position

# To pop element/item at spacific position use index with pop() method
teachers.pop(5) # it return the number 6
element
'Khalil'
```

### 8. Clear
``` python
# The clear() method remove all the elements from the list
teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil','Haris', 'Ihsan']
teachers.clear()
print(teachers)
[]
```

## Others Methods

### 9. Count
``` python 
# The count() method returns the number of elements/item with the specified value(itemname)
teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris', 'Ihsan']
count_teacher = teachers.count('Haris')
print(count_teacher)
2
```

### 10. Index
``` python
# The index() method returns the position/index at the first occurrence of the specified value(itemname)
teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris', 'Ihsan']
index_teacher = teachers.index('Irfan')
print(index_teacher)
```

### 11. Reverse

``` python
# The reverse() method reverses the order of the elements of the list
teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil', 'Haris', 'Ihsan']
teachers.reverse()
print(teachers)
['Ihsan', 'Haris', 'Khalil', 'Farhan', 'Sheraz', 'Haris', 'Irfan', 'Nasir']
```

### 12. Sort

``` python 
# Sort the list alphabetically
# The sort() method sorts the list ascending by default
teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil','Haris', 'Ihsan']
teachers.sort()

# Sorts the list in descending
teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil','Haris', 'Ihsan']
teachers.sort(reverse = True)
print(teachers)
```