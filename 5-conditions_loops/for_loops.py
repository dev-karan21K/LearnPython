#for loop

for i in range(1, 6):
    print(i)

print('--------')

fruits = ['Apple','Orange','lemon']
for fruit in fruits:
    print(fruit)
    
print('--------')  

word = "python"
for char in word:
    print(char)
    
print('--------')

my_dict = {
    'name':"karan",
    'age': 26,
    'city': "virudhunagar",
}

for key in my_dict:
    print(key)
    
print('--------')

for val in my_dict.values():
    print(val)
    
print('--------')


for key, val in my_dict.items():
    print(key, val)