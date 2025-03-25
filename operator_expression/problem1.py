#write a program to deside if the persion is eligible for loan or not
#Eligiblility Criteria: The persom should be more than 18 year's old, his income should be more than 30000

age = 25
income = 20000
is_eligible = age >= 18 and income > 30000
print(is_eligible)

""" 
check if someone can enter a park for free
They can enter if they are a child (age below 12) or a senior (age above 60)
"""

child_age = 72

is_entering_park_free = child_age < 12 or child_age >= 60

print(is_entering_park_free)