my_set_1 = {"Windows", "Linux", "Unix"}
my_set_2 = {"Windows", "Linux", "Mac OS"}


#intersection allows you to find common elements between two sets
print(my_set_1.intersection(my_set_2))


# difference finds the item that existed in the first set bu
# it does not exist in the other set

print(my_set_1.difference(my_set_2))
print(my_set_2.difference(my_set_1))