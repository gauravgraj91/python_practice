from webbrowser import get

price_lookup = {'apples' : 2.29,
                'Oranges' : 3.39,
                'Milk' : 2.99}

print(price_lookup['apples'])

d = {'K1' : 123,
'K2' : [0,1,2],
'K3' : {'insideKey' : 100}}

print(d['K2'][2])
print(d['K3']['insideKey'])

d2 = {'Key' : ['a','b','c']} 

### 2 is the index in the list key which is a dict of d2 that is converted to upper case using built in method.

print(d2['Key'][2].upper()) 

d2['Key'][0] = 'aa'
print(d2)
print(d.keys()) 
print(d.values())
print(d.items())

### Accessing Dictionay Items

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(thisdict["model"])

x = thisdict.get("year")
print(x)
x1 = thisdict.keys()
print(x1)
print(thisdict.values())

my_dict = {
    'key1' : 'val1',
    'key2' : 'val2',
    'key3' : 'val3'
}
print(my_dict['key1'])

my_dict2 = {
    'g1' : 123,
    'g2' : [0,1,2],
    'g3' : {'inside_key' : 100},
    'g4' : ['a', 'b', 'c', 'd']
}
print(my_dict2['g2'])
print(my_dict2['g3']['inside_key'])
print(my_dict['key1'].upper())
print(my_dict2['g4'][2].upper())
print(my_dict.keys()) 
print(my_dict2.values())
print(my_dict2.items())

