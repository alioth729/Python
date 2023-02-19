# Rahul Shah
# C0886666

# 4.1 Pizzas
favourite_pizzas = ["Pepperoni", "Margherita", "Double cheese"]

for pizza in favourite_pizzas:
    print("I like", pizza)
print("I really love pizza")

print("---------------------------------------")

# 4.2 Animals
favourite_animals = ["Lion", "Tiger", "Wolf"]

for animal in favourite_animals:
    print(f"A {animal} would make a great pet.")
print("These animals are on the top of the food chain")

print("---------------------------------------")

# 4.3 Counting to Twenty 
for count in range(1, 21):
    print(count)

store_number = []
for number in range(1, 1000001):
    store_number.append(number)
print(store_number)

print("---------------------------------------")

# 4.4 Summing a million
least_value = min(store_number)
highest_value = max(store_number)
print(f"The minimum value in a list of 1 million is {least_value}")
print(f"The maximum value in a list of 1 million is {highest_value}")
sum_value = sum(store_number)
print(f"The sum of number in the list in {sum_value}")

print("---------------------------------------")


# 4.6 Odd Numbers
odd_list = []
for i in range(1, 21):
    if i % 2 == 0:
        pass
    else:
        odd_list.append(i)
print(odd_list)


print("---------------------------------------")


# 4-13
buffet_style = ("Chicken Stir Fry", "Shrimp Stir Fry", "Pork Loin", "Chicken Alfredo", "Chicken and Rice")
for food in buffet_style:
    print(food)
try:
    buffet_style[0] = "Chicken"
except TypeError:
    print("TypeError: 'tuple' object does not support item assignment")

new_buffet_style = list(buffet_style)
new_buffet_style[0] = "Boneless Ribs Beef"
new_buffet_style[2] = "Sliced Beef"
buffet_style = tuple(new_buffet_style)
for food in buffet_style:
    print(food)

print("---------------------------------------")

# 8-3 T-Shirt
# 8-4 Large Shirts
def make_shirt(size="L", message="I love Python"):
    print(f"The size of the t-shirt is {size} and {message}")


make_shirt("M", "color is black")
make_shirt(message="blue", size="L")
make_shirt()
make_shirt(size="M")
make_shirt(size="S", message="I love DevOps")

print("---------------------------------------")

# 8-5 Cities
def describe_city(city, country = "Canada"):
    print(f"{city} is in {country}")


describe_city("Toronto")
describe_city("London", "England")
describe_city("New York", "USA")

print("---------------------------------------")

# 8-6 City-Country
def city_country(city, country):
    print(f'"{city}, {country}"')


city_country("Vancouver", "Canada")
city_country("Los Angeles", "USA")
city_country("Bangalore", "India")

print("---------------------------------------")

# 8-7 Album
# 8-8 User Albums
def make_album(artist_name, artist_title, no_of_songs = None):
    album_dictionary = {}
    album_dictionary["artist_name"] = artist_name
    album_dictionary["artist_title"] = artist_title
    album_dictionary["no_of_songs"] = no_of_songs
    return (album_dictionary)


print(make_album("Harry Styles", "Fine Line"))
print(make_album("Linda Ronstadt", "Heart Like a Wheel", 20))
print(make_album("Black Flag", "Damaged", 12))

enter_value = True
while(enter_value):
    artist_name = input("Enter artist name")
    artist_title = input("Enter artist title")
    print(make_album(artist_name,artist_title))
    ask_continue = input("Do you want to continue. Enter 'y' for yes or 'n' for no: ")
    if ask_continue.lower() == "n":
        enter_value = False

print("---------------------------------------")











