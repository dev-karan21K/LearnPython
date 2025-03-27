#List

my_list = [1,2,3,"apple","banana",True]
print(my_list)

my_list.append("cherry")
print(my_list)

my_list.extend([4,6])
print(my_list)

my_list.insert(3, "grape")
print(my_list)

my_list.remove("banana")
print(my_list)

my_list.pop(3)
print(my_list)


del my_list[1]
print(my_list)


#Slice
sub_list = my_list[2:6]
print(sub_list)

print(len(my_list))
print(len(sub_list))

print('apple' in my_list)