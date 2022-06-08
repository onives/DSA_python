import math
array_sample = [100, [10, 6, 6, 8], 2]


def solution(x, b, z):
    total = 0
    for ele in range(0, len(b)):
        total += b[ele]

    remaining = x - total

    if total == x:
        print("download completed!")
        return 0

    if z > len(b):
        average1 = total/len(b)
        return math.ceil(remaining/average1)

    count = z
    num_sum = 0
    while count > 0:
        num_sum += b.pop()
        count = count - 1

    average_now = num_sum/z

    return math.ceil(remaining/average_now)


solution(100, [10, 6, 6, 8], 5)
