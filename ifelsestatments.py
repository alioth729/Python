# C0886666
# Rahul Shah

# 5-1
country = "Canada"
print(f"Is country == 'USA'? I predict True.")
print(country == 'USA')

country = "Canada"
print(f"Is country == 'India'? I predict True.")
print(country == 'India')

country = "Canada"
print(f"Is country == 'Nepal'? I predict True.")
print(country == 'Nepal')

country = "Canada"
print(f"Is country == 'Sri Lanka'? I predict True.")
print(country == 'Sri Lanka')

country = "Canada"
print(f"Is country == 'Canada'? I predict True.")
print(country == 'Canada')

car = "BMW"
print(f"Is car == 'BMW'? I predict True.")
print(car == 'BMW')

book = "Game of Thrones"
print(f"Is book == 'Game of Thrones'? I predict True.")
print(book == 'Game of Thrones')

city = "Toronto"
print(f"Is city == 'Toronto'? I predict True.")
print(city == 'Toronto')

continent = "North America"
print(f"Is continent == 'North America'? I predict True.")
print(continent == 'North America')
print("------------------------------------------------------")

# 5-2

country = "Japan"
print(f"Equality operator check for False: {country== 'Canada'}")
print(f"Equality operator check for True: {country == 'Japan'}")
print(f"Inequality operator check for False: {country != 'Canada'}")
print(f"Inequality operator check for False: {country != 'Japan'}")
print(f"lower() method: {country.lower() == 'Japan'}")
print(f"lower() method: {country.lower() == 'japan'}")
print("-----------------------------------------")

magic_number = 2
print(f"Test for equality: {magic_number == 2}")
print(f"Test for inequality: {magic_number != 2}")
print(f"Test for greater than: {magic_number > 2}")
print(f"Test for less than: {magic_number < 2}")
print(f"Test for greater than or equal to: {magic_number >= 2}")
print(f"Test for less than or equal to: {magic_number <= 2}")
print(f"Test for equality: {magic_number == 4}")
print(f"Test for inequality: {magic_number != 4}")
print(f"Test for greater than: {magic_number > 4}")
print(f"Test for less than: {magic_number < 4}")
print(f"Test for greater than or equal to: {magic_number >= 4}")
print(f"Test for less than or equal to: {magic_number <= 4}")

test_list = ["car", "bus", "train"]
if "car" in test_list or "bike" in test_list:
    print("True if at least one value in list")

if "car" in test_list and "bike" in test_list:
    pass
else:
    print("True if only both item present in the list")

print("----------------------------------------------------")

# 5-3

alien_color = "green"
if alien_color == "green":
    print("You just earned 5 points")
print("---------------------------------------------")
# 5-4

if alien_color == "green":
    print("You just earned 5 points for shooting the alien.")
else:
    print("You just earned 10 points")

alien_color = 'yellow'
if alien_color == "green":
    print("You just earned 5 points for shooting the alien.")
else:
    print("You just earned 10 points")

print("---------------------------------------------")

# 5-5
alien_color_list = ["green", "yellow", "red"]
for color in alien_color_list:
    alien_color = color
    if alien_color == "green":
        print("You earned 5 points")
    elif alien_color == "yellow":
        print("You earned 10 points")
    elif alien_color == "red":
        print("You earned 15 points")

print("---------------------------------------------")

# 5-6
age = 25
if age < 2:
    print("You are a baby")
elif 2 <= age < 4:
    print("You are a toddler")
elif 4 <= age < 13:
    print("You are a kid")
elif 13 <= age < 20:
    print("You are a teenager")
elif 20 <= age < 65:
    print("You are an adult")
elif age >= 65:
    print("You are an elder")

print("---------------------------------------------")

# 5-7
favourite_fruits = ["Apple", "Mango", "Orange"]

if "Mango" in favourite_fruits:
    print("You really like Mangoes")

if "Strawberry" not in favourite_fruits:
    print("You do not like Strawberries")

if "Mango" in favourite_fruits:
    print("You really like Mangoes")

if "Orange" in favourite_fruits:
    print("You really like Oranges")

if "Dragonfruit" in favourite_fruits:
    print("You do not like Dragonfruit")

print("---------------------------------------------")

# 5-8
username_list = ["admin", "Mr. T", "aragon", "Mr. P", "ghost"]
for username in username_list:
    if username == "admin":
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")
print(username_list)

print("---------------------------------------------")

# 5-9
if len(username_list) > 0:
    print("The list is not empty")
    username_list.clear()
if len(username_list) < 1:
    print("We need to find some users!")

print("---------------------------------------------")

# 5-10

current_users = ["alioth", "dark_knight", "ghost", "ace", "sparrow"]
new_users = ["yolo", "ace", "sparrow", "epic", "faker"]
for new in new_users:
    for used in current_users:
        if new.lower() == used.lower():
            print(f"{new} username has already been used. Enter a new username")
    if new not in current_users:
        print(f"{new} username is available")

print("---------------------------------------------")

# 5-11
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for ordinal in number_list:
    if ordinal == 1:
        print(f"{ordinal}st")

    elif ordinal == 2:
        print(f"{ordinal}nd")

    elif ordinal == 3:
        print(f"{ordinal}rd")

    else:
        print(f"{ordinal}th")

print("---------------------------------------------")
