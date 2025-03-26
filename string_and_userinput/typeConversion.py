#Type Conversion


#calculating someone's age from their birth year
birth_year = int(input('Enter your birth year: '))
current_year = 2025
age = current_year - birth_year
print('Your age is: ', age)

#Calculate the price of tax
price = float(input('Enter the price of product: '))
tax_rate = 0.15
total_price = price + (price * tax_rate)
print(total_price)

fruits = ('apple','orange','banana')
fruits_list = list(fruits)
fruits_list.append('cherry')
print(fruits_list)

mutable_list = ['python','Django','React']
immutable_tuple = tuple(mutable_list)
print(immutable_tuple)

age = 20
message = "you are "+ str(age) + " years old"
print(message)


is_member = True
discount = 5 * int(is_member)
print('your discount amount is: ', discount)