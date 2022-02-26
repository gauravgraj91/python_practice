list1 = ["apple", "banana", "mango"]
list2 = [1, 2, 3, 4, 5]
list3 = [True, False, True, True]

print(type(list1))
print(len(list2))
print(list3[0:])
print(list2+list3)

list2[0] = 0
print(list2)

list2.append(6)
print(list2)

list2.pop(1)
print(list2)

new_list = ['a','e','i','o','u']
new_list2 = [4,2,8,1,6]

print(new_list.reverse())
print(new_list2.sort())
print(new_list + new_list2)