# Creating a tuple
my_tuple = (1, 2, 3, 4, 2)
print("Original tuple:", my_tuple)
# count() – counts occurrences of a value
count_of_2 = my_tuple.count(2)
print("Count of 2:", count_of_2)
# index() – returns index of first occurrence
index_of_3 = my_tuple.index(3)
print("Index of 3:", index_of_3)

# len() – returns length of tuple
print("Length of tuple:", len(my_tuple))

# min() and max()
print("Minimum value:", min(my_tuple))
print("Maximum value:", max(my_tuple))

# sum() – sum of elements
print("Sum of elements:", sum(my_tuple))

# slicing
sub_tuple = my_tuple[1:4]
print("Sliced tuple:", sub_tuple)

# nested tuple
nested_tuple = (my_tuple, (5, 6, 7))
print("Nested tuple:", nested_tuple)

# tuple unpacking
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)

# converting tuple to list (for modification)
temp_list = list(my_tuple)
temp_list.append(10)
modified_tuple = tuple(temp_list)
print("Tuple after conversion & modification:", modified_tuple)

# checking membership
print("Is 3 in tuple?", 3 in my_tuple)
print("Is 9 in tuple?", 9 in my_tuple)
