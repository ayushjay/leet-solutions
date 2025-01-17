# insert at end

def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n
myArr = [1,2,3,4,None,None]


insertEnd(myArr, 5,4,6)
print (myArr)


# inserting at ith index

def insertMiddle(arr, i, n, length):
# Shift starting from the end to i.
    for index in range(length - 1, i - 1,-1):
        # swap adjacent in reverse order
        arr[index + 1] = arr[index]
        # Insert at i
    arr[i] = n

myArr2 = [1,2,3,None, None]
insertMiddle(myArr2,3,4,4)

print(myArr2)

# Remove value at index i before shifting elements to the left.
# Assuming i is a valid index.
def removeMiddle(arr, i, length):
    # Shift starting from i + 1 to end.
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
    # No need to 'remove' arr[i], since we already shifted


myArr3 = [1,2,33,3,4,5,6,None]
print(len(myArr3))
removeMiddle(myArr3,2,8)
print(myArr3)
# key Takeaway: None is included in len() parameter