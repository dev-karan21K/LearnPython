#handling dictionary csv
import csv

# with open('data.csv', 'r') as file:
#     content = csv.DictReader(file)
#     for row in content:
#         print(row)
        
newdata = [
    {"Name":"karan", "Email": "karanbose1999@gmail.com", "Gender": "Male"},
    {"Name":"bose", "Email": "bose1999@gmail.com", "Gender": "Male"},
]
with open('new_dict.csv', 'w') as file:
    fieldnames = ["Name","Email","Gender"]
    content = csv.DictWriter(file, fieldnames=fieldnames)
    content.writeheader()
    content.writerows(newdata)