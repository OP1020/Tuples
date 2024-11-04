#SECTION 1
fruit_tuple = ("apple", "banana", "cherry", "date")
print(fruit_tuple[0])
print(fruit_tuple[-1])
slice_tuple = fruit_tuple[1:3]
print(slice_tuple)

#SECTION 2
num_tuple = (3, 5, 3, 2, 8, 3, 7)
#TODO: look at the count method in the notes
print(num_tuple.count(3))
#TODO: Look at the index method in the notes
print(num_tuple.index(8))

#SECTION 3
person_info = ("Alice", 28, "Engineer")
#TODO: Look at the notes for unpacking
name, age, profession = person_info
print(name)
print(age)
print(profession)
#TODO: print the variables.
