import datetime

now_date = datetime.datetime.now().strftime("%Y")
print(now_date)

arr = [None] * 5
arr1 = [[None]] * 5
arr1[0][0] = "six"
arr[1] = "six"
arr.append("four")
# arr1[].append("six")
print(arr)
print(arr1)
