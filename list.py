my_list = ["Windows", "Linux", "Mac OS", "Unix"]
print(my_list)
print(type(my_list))
# List[Index]
# Index in Python starts from 0 and it goes until the len(List)
print("The second element of my_list: ", my_list[1])
print("Length of my_list: ", len(my_list))
print("The last element of my_list: ", my_list[-1])

print(my_list[0:2])
# 0 mean start the search from the beginning of my_list
# my_list[0] -> Windows
# 0 + 1 = 1
# my_list[1] -> Linux
# 1 + 1 =2

print(my_list[-2:-1])
# negative index means come to the end of my list
# start from -2 -> my_list[-2]
# -2 + 1 = -1

# List[START_POINT:END_POINT:STEP_SIZE]
print(my_list[0:3:2])

# List can be nested
nested_list = [1, 2, 3, [4, 5, 6]]
print(len(nested_list))
# nested_list[3] -> List
print(nested_list[3])
print(len(nested_list[3]))
my_list_2 = nested_list[3]
print(my_list_2[0])