fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)


list_a = [1, 2, 3]
list_b = list_a
list_a[0] = 999
print(list_b)

fruits = ["apple", "banana"]
new_fruits = fruits.append("cherry")
print(new_fruits)
print(fruits)