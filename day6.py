# dict

data = {
    "name": "Nabraj",
    "age": 22
}
print(data)
print(data["name"])
print(data["age"])
print(type(data))
print(len(data))



data2 = {
    "name": ["Nabraj", "Hello"],
    "phone": 9809438442
}
print(data2["name"][-2])   # Nabraj


data3 = {
    "name": {
        "address":"Dang"
    },
    "phone": 987454121201
}
print(data3["name"]["address"])


data4 = [
    {
        "name":"Nabraj",
        "phone_number": [
            {
                "name":"NTC",
                "number": 9745612322
            },
            {
                "name": "Ncell",
                "number": 9809438442
            }
        ]
    }
]
for  i in data4:
    name = i["name"]
    print(i["phone_number"])
    for j in i["phone_number"]:
        print(f'{name} {j["name"]} number is {j["number"]}')
        
        
print('_______________________________________')

data = {
    'type': "NTC",
    'phone': "9809745515"
}

data['sdasdasda'] = 64516
print(data)

data.update({'phone': "this is update", 'suman': "hello"})
print(data)

del data['phone']
print(data)


data.pop("type")
print(data)

data.popitem()
print(data)




data6 = {
    "name": "Suman",
    "test": "testing"
}
print(data6.keys())
print(data6.values())