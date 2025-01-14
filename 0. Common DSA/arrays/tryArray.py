# insert at end

def insertEnd(arr, ele):
    # in python doing arr[len(arr)] = ele throws IndexError
    arr[len(arr) - 1] = ele
myArr = [1,2,3,4]


insertEnd(myArr, 5)
print (myArr)


# inserting at ith index

def insertMiddle(arr, i, n, length):
# Shift starting from the end to i.
    for index in range(length - 1, i - 1,-1):
        # swap adjacent in reverse order
        arr[index + 1] = arr[index]
        # Insert at i
    arr[i] = n

myArr2 = [1,2,3,None,None]
insertMiddle(myArr2,3,4,4)

print(myArr2)