def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n

def removeEnd(arr,length):
    if length > 0:
        arr[length - 1] = 0


def insertMiddle(arr, n, index, length):
    for i in range(length - 1, index - 1, -1):
        arr[i + 1] = arr[i]
    arr[index] = n

def removeMiddle(arr, i, length):
    for index in range(i+1, length):
        arr[index - 1] = arr[index]
    
def printArr(arr, capacity):
    for i in range(capacity):
        print(arr[i])