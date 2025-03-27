#Sets

my_set = {1,2,3,"apple","banana",False}

dub_list = [1,3,5,4,4,6,3,1,1]
another_set = set(dub_list)
print(another_set)

my_set.add("orange")
print(my_set)

my_set.remove(False)
print(my_set)

# my_set.remove("cherry")
# print(my_set)

my_set.discard("mango")
print(my_set)


#union
set1 = {1,2,3}
set2 = {3,4,5}

union_set1 = set1.union(set2)
union_set2 = set1 | set2
print(union_set1)
print(union_set2)

#intersection
intersection_set1 = set1.intersection(set2)
intersection_set2 = set1 & set2
print(intersection_set1)
print(intersection_set2)

#difference
difference_set1 = set1.difference(set2)
difference_set2 = set1 - set2
print(difference_set1)
print(difference_set2)

box1 = {'car','ball','doll','robot'}
box2 = {'doll','robot','train'}

unique_to_box1 = box1 - box2
print(unique_to_box1)