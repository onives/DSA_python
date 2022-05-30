from collections import deque

# # implementation using a list
# stack = []  # use append() and pop() O(1)
# # can run into speed issues as it grows. so some append calls will be slower than the rest
#
# # implementation using collections.deque
# # Deque is preferred over the list in the cases where we need quicker append and
# # pop operations from both the ends of the container, as deque provides an O(1) time complexity
# # for append and pop operations as compared to list which provides O(n) time complexity.
#
# stack_2 = deque()
# stack_2.append(1)
# stack_2.append(2)
# stack_2.append(3)
# stack_2.append(4)
# # print(stack_2)
# print(stack_2.pop())
# print(stack_2.pop())
# print(stack_2)
#
#
# # Implementation using queue
# # Queue module also has a LIFO Queue, which is basically a Stack.
#
#
# # Reverse a string using stack
# string_one = "forever"
# stack_two = deque()
# string_reversed = ""
#
# for _ in range(0, len(string_one)):
#     stack_two.append(string_one[_])
#
# # for _ in string_one:
# #     stack_two.append(_)
#
# while len(stack_two) != 0:
#     string_reversed += stack_two.pop()
#
# print(stack_two)
# print(string_one)
# print(string_reversed)


# Parenthesis checker
string_three = "One{}[()]"
string_four = "two ([]"
string_five = "yes {}]"


def par_checker(string):
    stack_3 = deque()
    opening_ = ["(", "{", "["]
    closing_ = [")", "}", "]"]
