#data types in python
#String, Number (integers & Floating point numbers), Boolean, List, Tuple, Dictionary, Set

num = 10
num2 = 10.5
is_active = True

fruits = ['banana','orange','apple']
num = [1,2,3,4,5]
fruits[1] = 'lemon'
print(fruits)
print(num)



print('--------------tuple-----------------')
fruits_tuple = ('banana','orange','apple')
#fruits_tuple[1] = 'Lemon' -----> not compile this line of code
print(fruits_tuple)



print('--------------dict-----------------')
test_dict = {
    'name': 'karan',
    'age': 26,
}

print(test_dict)


print('--------------set-----------------')
test_set = {'karan','john',1,2,'bose','karan'}
print(test_set)