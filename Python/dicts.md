## Python Dictionaries

Dictionaries are used to store data values in key:value pairs.Dictionaries are created by enclosing
a comma-separated list of key-value pairs in curly braces { }.

```python
# Create a dictionary of boy details
boy = {
        'Name': 'Ali',
        'Age': 21,
        'Height': 6,
        'Weight': 68,
        'City':'Peshawar',
        'Religion': 'Muslim'
    }
print(boy)
{
    'Name': 'Ali',
    'Age': 21,
    'Height': 6,
    'Weight': 68,
    'City':'Peshawar',
    'Religion': 'Muslim'
}
```

### Dictionary Items

Dictionary items are ordered, muteable(changeable), and does not allow duplicates.

```python

# Create a dictionary to show dictionary items are ordered and can not allow duplicate
boy = {'Name': 'Ali', 'Age': 21, 'Hieght': 6, 'Weight': 68, 'City':
'Islamabad', 'City': 'Peshawar', 'Religion': 'Muslim'}
print(boy)
{'Name': 'Ali', 'Age': 21, 'Hieght': 6, 'Weight': 68, 'City':
'Peshawar', 'Religion': 'Muslim'}
# change the value in the dictionary
boy['Age'] = 23
print(boy)
{'Name': 'Ali', 'Age': 23, 'Hieght': 6, 'Weight': 68, 'City':
'Peshawar', 'Religion': 'Muslim'}
# The update() method is also used to change the the value in the
dictionary
boy.update({'Age': 22})
print(boy)
{'Name': 'Ali', 'Age': 22, 'Hieght': 6, 'Weight': 68, 'City':
'Peshawar', 'Religion': 'Muslim'}
```

### Dictionary Length

```python
# To determine how many items dictionary have, use the len() function
print(len(boy))
```

### Accessing dictionary Items/Values

```python
# Access the items of a dictionary by referring to its key name, inside square brackets
boy = {'Name': 'Ali', 'Age': 21, 'Hieght': 6, 'Weight': 68, 'City':
'Islamabad', 'City': 'Peshawar', 'Religion': 'Muslim'}
# Access the city
city = boy['City']
print(city)
Peshawar
# There is also a method called get() that will give you the same result
religion = boy.get('Religion')
print(religion)
Muslim

```

### Add Dictionary Items

```python
# Adding an item to the dictionary is done by using a new index key and assigning a value to it
boy = {'Name': 'Ali', 'Age': 21, 'Hight': 6.3, 'Weight': 68, 'City':
'Islamabad', 'City': 'Peshawar'}
# add religion to the dictionary
boy['Religion'] = 'Muslim' # This will add the 'Religion' key-value pair to the end of the dictionary
print(boy)
{'Name': 'Ali', 'Age': 21, 'Hight': 6.3, 'Weight': 68, 'City':
'Peshawar', 'Religion': 'Muslim'}
```

### Python Dictionary Methods

```python
# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added to the dictionary.
boy = {'Name': 'Ali', 'Age': 21, 'Hight': 6.3, 'Weight': 68, 'City':
'Islamabad', 'City': 'Peshawar'}
# Updated the dictionary with the Religion as key and Muslim as value
boy.update({'Religion': 'Muslim'})
print(boy)
{'Name': 'Ali', 'Age': 21, 'Hight': 6.3, 'Weight': 68, 'City':
'Peshawar', 'Religion': 'Muslim'}

```

### Remove Dictionary Items

#### 1. Del

```python
# The del keyword removes the item with the specified key name
boy = {'Name': 'Ali', 'Age': 21, 'Hieght': 6, 'Weight': 68, 'City':'Peshawar', 'Religion': 'Muslim'}
# delete any item from the dictionary
del boy['Hieght']
print(boy)
{'Name': 'Ali', 'Age': 21, 'Weight': 68, 'City': 'Peshawar','Religion': 'Muslim'}
# The del keyword can also delete the dictionary completely
boy = {'Name': 'Ali', 'Age': 21, 'Hieght': 6, 'Weight': 68, 'City':'Peshawar', 'Religion': 'Muslim'}
# delete the dictionary
del boy
print(boy) # This will cause an error because the dictionary boy no longer exists
----------------------------------------------------------------------
-----
NameError Traceback (most recent call
last)
Cell In[63], line 7
 4 # delete the dictionary
 5 del boy
----> 7 print(boy)
NameError: name 'boy' is not defined
```

#### 2. Pop

```python
# the pop() method removes the item with the specified key name
boy = {'Name': 'Ali', 'Age': 21, 'Hieght': 6, 'Weight': 68, 'City':
'Peshawar', 'Religion': 'Muslim'}
# remove any item from the dictionary
boy.pop('Weight')
print(boy)
{'Name': 'Ali', 'Age': 21, 'Hieght': 6, 'City': 'Peshawar',
'Religion': 'Muslim'}
```

#### 3. Popitem

```python
# The popitem() method removes the last inserted item
boy = {'Name': 'Ali', 'Age': 21, 'Hieght': 6, 'Weight': 68, 'City':
'Peshawar', 'Religion': 'Muslim'}
# remove the last item of the dictionary
boy.popitem()
print(boy)
{'Name': 'Ali', 'Age': 21, 'Hieght': 6, 'Weight': 68, 'City':
'Peshawar'}
```

#### 4.Clear

```python
# The clear() method empties the dictionary
boy = {'Name': 'Ali', 'Age': 21, 'Hieght': 6, 'Weight': 68, 'City':
'Peshawar', 'Religion': 'Muslim'}
# Empty the dictionary
boy.clear()
print(boy)
{}
```

#### 5. Copy

```python
# The copy() method returns a copy of the specified dictionary
boy = {'Name': 'Ali', 'Age': 21, 'Hieght': 6, 'Weight': 68, 'City':
'Peshawar', 'Religion': 'Muslim'}
# copy the boy dictionary
boy_new = boy.copy()
print(boy_new)
{'Name': 'Ali', 'Age': 21, 'Hieght': 6, 'Weight': 68, 'City':
'Peshawar', 'Religion': 'Muslim'}
```

#### 6. Get

```python
# The get() method returns the value of the item with the specified
key
boy = {'Name': 'Ali', 'Age': 21, 'Hieght': 6.7, 'Weight': 69, 'City':
'Peshawar', 'Religion': "Muslim"}
# get the value of the item
city = boy.get('City')
print(city)
Peshawar
# Try to return the value of an item that do not exist
education = boy.get('education','Undergraduate')
print(education)
Undergraduate
```

#### 7. Keys

```python
# The keys() method returns the keys of the dictionary as a list
boy = {'Name': 'Ali', 'Age': 21, 'Hieght': 6.7, 'Weight': 69, 'City':
'Peshawar', 'Religion': "Muslim"}
# Get the keys of the dictionary
dict_keys = boy.keys()
print(dict_keys)
dict_keys(['Name', 'Age', 'Hieght', 'Weight', 'City', 'Religion'])
```

#### 8. Values

```python
# The values() method returns the values of the dictionary as a list
boy = {'Name': 'Ali', 'Age': 21, 'Hieght': 6.7, 'Weight': 69, 'City':
'Peshawar', 'Religion': "Muslim"}
# Get the values of the dictionary
dict_values = boy.values()
print(dict_values)
dict_values(['Ali', 21, 6.7, 69, 'Peshawar', 'Muslim'])
```

## Nested Dictionaries

A dictionary can contain dictionaries, this is called nested dictionaries.

```python
# Create a dictionary that contain three dictionaries
boys_details = {'boy1' : {'Name': 'Ali', 'Age': 23, 'Hieght': 6.7,
'Weight': 69, 'City': 'Peshawar', 'Religion': "Muslim"},
 'boy2' : {'Name': 'Ahmad', 'Age': 21, 'Hieght': 6.5,
'Weight': 70, 'City': 'Peshawar', 'Religion': "Muslim"},
 'boy3' : {'Name': 'Abas', 'Age': 22, 'Hieght': 6.4,
'Weight': 72, 'City': 'Peshawar', 'Religion': "Muslim"}}

print(boys_details)
{'boy1': {'Name': 'Ali', 'Age': 23, 'Hieght': 6.7, 'Weight': 69,
'City': 'Peshawar', 'Religion': 'Muslim'}, 'boy2': {'Name': 'Ahmad',
'Age': 21, 'Hieght': 6.5, 'Weight': 70, 'City': 'Peshawar',
'Religion': 'Muslim'}, 'boy3': {'Name': 'Abas', 'Age': 22, 'Hieght':
6.4, 'Weight': 72, 'City': 'Peshawar', 'Religion': 'Muslim'}}

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries
boy1 = {'Name': 'Ali', 'Age': 23, 'Hieght': 6.7, 'Weight': 69, 'City':
'Peshawar', 'Religion': "Muslim"},
boy2 = {'Name': 'Ahmad', 'Age': 21, 'Hieght': 6.5, 'Weight': 70,
'City': 'Peshawar', 'Religion': "Muslim"},
boy3 = {'Name': 'Abas', 'Age': 22, 'Hieght': 6.4, 'Weight': 72,
'City': 'Peshawar', 'Religion': "Muslim"}

# create a dictionary that contain the all three dictionaries
boys_detail = {
 'boy1' : boy1,
 'boy2' : boy2,
 'boy3' : boy3,
}
print(boys_detail)

{'boy1': ({'Name': 'Ali', 'Age': 23, 'Hieght': 6.7, 'Weight': 69,
'City': 'Peshawar', 'Religion': 'Muslim'},), 'boy2': ({'Name':
'Ahmad', 'Age': 21, 'Hieght': 6.5, 'Weight': 70, 'City': 'Peshawar',
'Religion': 'Muslim'},), 'boy3': {'Name': 'Abas', 'Age': 22, 'Hieght':
6.4, 'Weight': 72, 'City': 'Peshawar', 'Religion': 'Muslim'}}
```

## Access Items in Nested Dictionaries

```python
# To access items from a nested dictionary, you use the name of the
dictionaries, starting with the outer dictionary
boys_details = {'boy1' : {'Name': 'Ali', 'Age': 23, 'Hieght': 6.7,
'Weight': 69, 'City': 'Peshawar', 'Religion': "Muslim"},
 'boy2' : {'Name': 'Ahmad', 'Age': 21, 'Hieght': 6.5,
'Weight': 70, 'City': 'Peshawar', 'Religion': "Muslim"},
 'boy3' : {'Name': 'Abas', 'Age': 22, 'Hieght': 6.4,
'Weight': 72, 'City': 'Peshawar', 'Religion': "Muslim"}}
# Acess the boy2 name
boy2_name = boys_details['boy2']['Name']
print(boy2_name)
Ahmad
```
