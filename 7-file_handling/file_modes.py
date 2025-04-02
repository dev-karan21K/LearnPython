#file modes

#write mode
file = open('example.txt', "w")
file.write('write a program daily')
file.close()

#append mode
file = open('example.txt', 'a')
file.write("\n To solving problem continue...")
file.close()

#exclusive creation mode 
try:
    file = open('example1.txt', 'x')
    file.write('jioiejeiojoejiej')
    file.close()
except FileExistsError:
    print("file already exists")