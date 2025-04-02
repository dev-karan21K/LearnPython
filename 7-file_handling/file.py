#file handling

#syntax  ---> file = open("example.txt", "file mode")


file = open("example.txt", "r") # or file = open("example.txt", "rt")
content = file.read()
print(content)
file.close()