"""
    write a function indexEqualsValue that returns
    the lowest index for which array[index] == index. Return -1 if there is no such index.

    Examples:

    input: [-8,0,2,5]
    output: 2   # since array[2] == 2

    input: [-1,0,3,6]
    output: -1   # since no index in array satisfies array[index] == index
"""

# 1) iterate through passed list

intArr = [-1, 4, 6, 3, 4, 7, 5, 1]

def indexEqualsValue(arr):
    arr.sort()
    for index,number in enumerate(arr):
        if number == index:
            return number
    return -1
print(indexEqualsValue(intArr))
