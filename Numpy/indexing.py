import numpy as np

numberss = np.array([0,5,10,15,20,25,30])

result = numberss[5]

result = numberss[-1]

result = numberss[:3]
result = numberss[3:]
result = numberss[::]
result = numberss[::-1]
# print(result)

arr1 = np.arange(0,10)
arr2 = arr1

arr2[0] = 20

print(arr1)
print(arr2)