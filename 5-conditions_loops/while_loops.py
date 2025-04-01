#while loop


count = 1
while count <= 5:
    print(count)
    count += 1
    
print('--------')

is_running = True
while is_running:
    user_input =  input("Type 'stop' to end executing... : ")
    if user_input == 'stop':
        is_running = False