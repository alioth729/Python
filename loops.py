# def <FUNCTION_NAME>(INPUTS[OPTIONAL]):
# ...
# RETURN <RESULT> [OPTIONAL]

# f(x) = x ^ 2
def f(x):
    return x * x

# f(2) = 2 ^ 2 = 4
# print(f(2))
def f(x):
    print("The input is :" , x)
    print("And x^2 is: ", x * x)
    # return []

print(f(2))
# If your function does not have a return statement -> output is None

# None -  no container
# Null - container is empty

def f(x):
    print (x + x)

f(2)

w = 10 # a global variable
p = 5 # a global variable

def my_function(x):
    y = x * x # y is the varianle inside the function  -> private variable
    z = y + 1
    p = 20
    print("w is the flobal variables, so I can see that inside the function:", w)
    print("The value of p inside the function", p)
    return z

# print(p) # This returns an error because "p" is a private variable
my_function(x = 1)
print("The value of p outside of the function:", p)


# Input types of a function:
# 1) required inputs(s)
# optional inputs(s) -> there is a default value for this input

def my_function1(x, y = 5):
    print("The value of x is: ", x)
    print("The value of y is: ", y)

my_function1(x = 1) # the value of y is 5 (default value)
my_function1(x = 1, y = 10 ) # the value of y is 10 (I declared the new value)

def my_function2(x, y):
    print("The value of x is: ", x)
    print("The value of y is ", y)

my_function1(x = 1, y = [1, 2, 3])
my_function2(x = "John", y = {"key 1": 2, "key2": 3})


# The required arguments (inputs) always has to come first
# The optional arguments (inputs) always has to come last

def my_function3(z: int, x: str, y: list, w: int=0):
    """
    This function prnts the values of z, x, w, and y
    :param z: is a number between 0 and 100
    :param x: is a string
    :param w: is a number
    :param y: is a list
    :return: None
    """

    print("The value of z:", z)
    print("The value of x:", x)
    print("The value of w:", w)
    print("The value of y:", y)

my_function3(1, 2, [1, 2, 3])


# return <RESULT> [OPTIONAL]

# Create a calculator that can find the addition or suntraction between two numbers
# I need to have a master function for the calcultor 
# I need two sub-functions that provide addition or suntraction results

def my_calculator(a, b):
    print("The addition result is: ", find_addition(x = a, y = b))
    print("The subtraction result is:", find_subtraction(x = a, y = b))
    print("The multiplication result is:", find_multiplication(x = a, y = b))



def find_multiplication(x, y):
    z = x * y
    return z


def find_addition(x, y):
    z = x + y
    return z

def find_subtraction(x, y):
    z = x - y
    return z


my_calculator(a = 3, b = 5)
# This works because I have define "my_calculator", "find_addition", "find_subtraction" before this line




# Talk about iterations
# for <NAME_OF_ELEMENTS> in <ITERABLE_OBJECTS>:
# .....

my_list = ["1", 2, 3, 4]
for number in my_list:
    print(number)
    print(type(number))

for num in range(10):
    print(num)

my_dict = {"key 1": [1, 2, 3], "key 2": 5}
for key, value in my_dict.items():
    print("The key is:", key, " and the value is: ", value)


my_dict1 = {"key 1": [1, 2, 3], "Key 2": [8, 9, "J"]}
for key, value in my_dict1.items():
    print("The list that I have is: ", value)


    for element in value:
        print("The elements are: ", element)
    print("==================================== \n\n")