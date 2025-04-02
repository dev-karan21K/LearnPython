#binary file mode
file = open('sports.jpg', 'rb')
data = file.read()
print(data)
file.close()

#read and write 
file = open('example.txt', "r+")
content = file.read()
print(content)
file.write('\n Adding new line')
file.close()

#write and read
file = open('example.txt', "w+")
file.write("This will be overwrite the existing content")
file.seek(0)
content = file.read()
print(content)
file.close()

#append and read
file = open("example.txt", "a+")
file.write("\n Appending new content")
file.seek(0)
content = file.read()
print(content)
file.close()