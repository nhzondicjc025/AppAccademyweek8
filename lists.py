fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])

fruits[1] = "blueberry"
fruits.append("elderberry")
fruits.insert(2, "fig")
fruits.remove("date")
fruits.sort(reverse=True)
fruits.pop()
print(fruits)

#Tuples

my_tuple = (1, 2, 3, 4, 5)

print(my_tuple)
print(my_tuple[2])
print(my_tuple[1])
print(my_tuple[0])

tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

conc_tuple = tuple1 + tuple2
rep_tuple = tuple1 * 2

print(rep_tuple)

#Sets

my_set = {1, 2, 3, 4, 5}
my_set.add(6)
my_set.remove(2)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

#Union
union_set = set1.union(set2)
print(union_set)

# Intersection
inter_set = set1.intersection(set2)
print(inter_set)

# Difference
diff_set = set1.difference(set2)
print(diff_set)

my_dict = {"apple": 1, "banana": 2, "cherry": 3}
my_dict["date"] = 4
my_dict["banana"] = 7

print(my_dict)

