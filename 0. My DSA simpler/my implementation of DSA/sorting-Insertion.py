def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            # swap
            tmp = arr[j + 1] 
            arr[j + 1] = arr[j]
            arr[j] = tmp
            j = j - 1
    return arr

"""
what we're doing is
if arr is [1,4,2,89]
start at 4. then replace 4 by 2 and done
"""
array2 = [3,5,1,3,6,89,55,23,11]
print(insertionSort(array2))
