list_of_strings = ["Hello", "my", "friend"]

# bad way
my_string = ""
for i in list_of_strings:
    my_string += i + " "
print(my_string)

# good way
my_string = " ".join(list_of_strings)
print(my_string)