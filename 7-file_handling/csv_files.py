#csv files
import csv

#reading csv file without using with statement
file = open('data.csv', "r")
content = file.readlines()
print(content)
file.close()


# reading csv file using with statement
with open('data.csv', 'r') as file:
    content = file.readlines()
    print(content)


with open('data.csv', 'r') as file:
    content = csv.reader(file)
    for row in content:
        print(row)

data = [
    ['First Name', 'Last Name', 'Gender'],
    ['karan','bose','Male'],
    ['john','doe','Male'],
]

with open('new_data.csv', 'w') as file:
    content = csv.writer(file)
    content.writerows(data)
    
new_data = ['abc','abc@gmail.com','male']
with open('new_data.csv', 'a') as file:
    content = csv.writer(file)
    content.writerow(new_data)