#if elif else

age = 17
if age > 18:
    print('You are a minor')
elif age == 18:
    print("You became an adult")
else:
    print("You are an adult")
    
    
number = -1

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print('The number is zero')
    
    
#nested if
score = 87
if score >= 40:
    if score >= 90:
        print('Grade A')
    elif score >= 75:
        print('Grade B')
    elif score >= 60:
        print('Grade C')
    else:
        print("Grade D")
else:
    print('Failed')