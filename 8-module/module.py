from utilities import operations
from utilities import string_operations
import math
import random
from datetime import datetime
import time
import os
import sys
import json

# result = operations.add(10, 20)
# print(result)


# multiply_result = operations.multiply(10, 20)
# print(multiply_result)


# product_name = 'Shirt'
# uppercase_pro_name = string_operations.to_uppercase(product_name)
# lowercase_pro_name = string_operations.to_lowercase(product_name)

# print(uppercase_pro_name)
# print(lowercase_pro_name)

# print(math.sqrt(25))
# print(math.pi)


# print(random.randint(1, 100))
# print(random.choice([1,2,3,4,5,6,7,8,9,0]))
      

# now = datetime.now()
# print(now)
# print('Wait for 3 seconds...')
# time.sleep(3)
# print('done')


print(os.getcwd())

print(sys.version)

data = {
    'name': 'karan',
    'age': 25,
}
print(data)
json_string = json.dumps(data)
print(type(json_string))
print(json_string)