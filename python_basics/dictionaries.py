# setdefault() and get() and defaultdict

from collections import defaultdict
# Suppose We have a dict which recording the result of a examination:
table = {"Nick": "A", "Ada": "B", "Mike": "B", "Leo": "C", "Sandy": "D"}

# We want to convert it to a dict with grade -> list of names so that we can check
# how many students in each grade. The result will be:
# { "A" : ["Nick"], "B" : ["Ada", "Mike"], "C" : ["Leo"], "D" : ["Sandy"] }

grades = {}

for name, grade in table.items():
    # create a key of grade with a default value as a list, store the returned list as _names
    _names = grades.setdefault(grade, [])
    _names.append(name)  # append name to the created list _grade

print(grades)
print(type(grades))


# Using defaultdict
result = defaultdict(list)
for name, score in table.items():
    result[score].append(name)  # all keys have a default already

print(type(result))
print(result)
