# write a function called maxSubArraySum which accepts an array of integers and a number called n.
# The fn should calculate the maximum sum of n consecutive elements in the array
# using the sliding window technique

def max_subarray_sum(arr, num):
    max_sum = 0
    temp_sum = 0

    # get the sum of the first num numbers in the list
    for i in range(0, num):
        max_sum += arr[i]

    temp_sum = max_sum
    for j in range(num, len(arr)):
        temp_sum = temp_sum + arr[j] - arr[j - num]
        if temp_sum > max_sum:
            max_sum = temp_sum
        # print(temp_sum, max_sum)
    return max_sum


print(max_subarray_sum([3,4,5,1,6,1,6,2,8,1,9,0,2,3,6,1], 3))
