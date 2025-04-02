#read a file using with statement (context manager)

# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)
    
    
with open('example.txt', 'w') as file:
    file.write("Hello, Python")