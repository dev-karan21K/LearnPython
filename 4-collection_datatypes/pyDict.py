#Dictionary

my_dict = {"name": "Rathan", "age": 70, "city": "chennai"}
print(my_dict["name"])

print(my_dict.get("country", "Not Found"))
print(my_dict)

my_dict["age"] = 75
print(my_dict)

my_dict["country"] = "India"
print(my_dict)

my_dict.pop("city")
print(my_dict)


for key, value in my_dict.items():
    print(f"{key}   : {value}")
    
    
    
print("name" in my_dict)