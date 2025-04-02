#map function

#syntax ---> map(function, iterable..)
numbers = [1,2,3,4,5]
doubled = map(lambda x : x * 2, numbers)
print(list(doubled))

fruits = ['apple','orange','banana']
uppercase_fruits = map(str.upper,fruits)
print(list(uppercase_fruits))