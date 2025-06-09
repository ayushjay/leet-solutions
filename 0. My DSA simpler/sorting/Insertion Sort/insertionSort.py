# Python implementation of Insertion Sort
# stable sorting algo ie preserverse original order when two numbers are of same value like 7,2,7,8,56

def insertionSort(arr):
	# Traverse through 1 to len(arr)
    # Start at 1st Index
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            # arr[j] and arr[j + 1] are out of order so swap them 
            # j >= 0 keeps it in bounce, no index error
            #  SWAP
            tmp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = tmp
            j -= 1
    return arr