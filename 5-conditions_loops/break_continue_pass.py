#break continue pass

for number in range(1, 10):
    if number == 5:
        print(f"The number is {number} and stopping the loop")
        break
    print(number)
print('stopped')


for number in range(1, 10):
    if number %2 == 0:
        continue
    print(number)
print('stopped')


for number in range(1, 10):
    if number == 3:
        pass
    else:
        print(number)