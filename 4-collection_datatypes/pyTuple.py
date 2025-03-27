#Tuple

fruits = ("apple","banana","orange","cherry","berry")
print(fruits)

print(fruits[1:])
print(fruits[1:4])
print(fruits[:3])

tuple1 = (1,2,3)
tuple2 = (4,5,6)
combined_tuple = tuple1 + tuple2 
print(combined_tuple)

repeated = (1,2) * 10
print(repeated)

words = ("hello","world","hello","again","hello")
print(words.count("hello"))

single_tuple = (2,)

print(len(words))

numbers = (1,4,7,3,8,5)
print(max(numbers))
print(min(numbers))

print(sum(numbers))