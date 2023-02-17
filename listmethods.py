my_list = ["Windows", "Linux", "Mac OS", "Unix"]
# Add element to a list one at a time
# append(element)
my_list.append(["Windows 10", "Windows 7"])
print("------------------------------------------------------------------------")

# Add element at a specific index
# insert (index, element)
my_list.insert(0, "Windows")
print(my_list)
print("-----------------------------------------------------------------------")

# Get the index of an element
# index(element)
# index(element, start_point(optional), end_point(optional))
print(my_list.index("Windows", 0, 3))
print("-------------------------------------------------------------------------")

# count(element)
print(my_list.count("Windows"))
print("----------------------------------------------------------------------")

# Remove elements inside a list
# remove(element)
my_list.remove("Windows")
print(my_list)

# pop
my_list.pop(1)
print(my_list)
