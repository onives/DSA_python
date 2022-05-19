import re
my_string = "From nives@gmail.com i have been doing fine"
my_second_string = " I have an email carol@yahoo.com but I am not sure"
third_string = "Copyright 2011 all rights reserved,blablabla"
third_string2 = "Copyright 20290 nn all rights reserved, Copyright 2018 blablabla"

# return the host name from a string
def return_host(string):
    at_index = string.find('@')
    space_index = string.find(" ", at_index)
    host_name = string[at_index+1: space_index]
    return host_name


def return_host(string):
    _pattern = "Copyright 20[0-9]+"
    string2 = re.sub(_pattern, "Copyright 2022", string)
    print(string2)


# # Reverse a string and check palindrone
def palindrone_solution(inputString):
    # reversed_string = inputString[::-1]  # one method to reverse string
    reversed_string = "".join(reversed(inputString))  # another mtd to reverse string
    return inputString == reversed_string


print(palindrone_solution("aabaa"))
