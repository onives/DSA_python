# given two strings, write a function to determine if the second string
# is an anagram of the first

def is_anagram(string1, string2):
    string1_dict = {}
    string2_dict = {}

    if len(string1) != len(string2):
        return False

    for char in string1:
        string1_dict[char] = string1_dict.get(char, 0) + 1

    for char in string2:
        string2_dict[char] = string2_dict.get(char, 0) + 1

    for key in string1_dict:
        if string1_dict[key] != string2_dict.get(key, 0):
            return False
    return True


# print(is_anagram("nives", "knives"))
# print(is_anagram("car", "rat"))
print(is_anagram("full", "lufl"))
