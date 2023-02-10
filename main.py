# RAHUL SHAH
# C0886666

# 2-1. Simple Message: Assign a message to a variable, and then print that message.
print("Q.2-1. Simple Message")
first_display = "Welcome to Canada"
print(first_display)
print("------------------------------------------------------------------------")


# 2-2. Simple Message: Assign a message to a variable, and print that message.
# Then change the value of the variable to a new message, and print
# the new message.
print("Q.2-2.Simple Messages")
primary_value = "It's -20C today"
print(primary_value)
primary_value = "It feels like -30C today"
print(primary_value)
print("-------------------------------------------------------------------------")

# 2-3 Personal Message: Use a variable to represent a person's name, and print
# a message to that person. Your message should be simple, such as, "Hello Eric,
# would you like to learn Python today?"
print("Q.2-3 Personal Message")
your_name = "Jessica"
print("Hello {}, would you like to learn some Python today?".format(your_name))
print("--------------------------------------------------------------------------")

# 2-4 Name Cases: Use a variable to represent a person's name, and then print
# that person's name in lowercase, uppercase, and title case.
print("Q.2-4 Name Case")
name_case = "Albert Einstein"
print(name_case.lower())
print(name_case.upper())
print(name_case.title())
print("-----------------------------------------------------------------------------")
# 2-5 Famous Quote: Fina a quote from a famous person you admire. Print the
# quote and the name of its author.
print("Q.2-5 Famous Quote")
print('Nelson Mandela once said, "The greatest glory in living '
      'lies not in never falling, but in rising every time we '
      'fall."')
print("--------------------------------------------------------------------------------")

# 2-6 Famous Quote 2:Repeat exercise 2-5 but this time, represent the famous person's name
# using a variable called famous_person. Then compose your message and represent it with a
# new variable called message. Print your message.
print("Q.2-6 Famous Quote 2")
famous_person = "Nelson Mandela"
message = '"The greatest glory in living ' \
          'lies not in never falling, but in ' \
          'rising every time we fall."'
print(famous_person + " " + "once said, " + message)
print("----------------------------------------------------------------------------------------")


# 2-7 Stripping Names
print("Q.2-7 Stripping Names")
person_name = "\tNelson Mandela\n"
print(person_name)
print(person_name.lstrip())
print(person_name.rstrip())
print(person_name.strip())
print("-----------------------------------------------------------------------------------------")

# 2-8
print("Q.2-8. Number Eight")
print(2 + 6)
print(10 - 2)
print(1 * 8)
print(16 / 2)
print("------------------------------------------------------------------------------------------")

# 2-9. Favourite Number
print("Q.2-9 Favourite Number")
favourite_number = 2
print("My favourite number is {}".format(favourite_number))
print("--------------------------------------------------------------------------------------------")
