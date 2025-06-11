def mergeSort(arr,s,e):
    # length of arr
    if e - s + 1 <= 1:
        return arr
    
    m = (s + e) // 2

    mergeSort(arr,s,m) 
    mergeSort(arr,m+1,e)

    merge(arr,s,m,e)

    return arr

def merge(arr,s,m,e):

    L = arr[s:m+1]
    R = arr[m+1:e+1]

    i = 0
    j = 0
    k = s

    while i<len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j +=1
        k += 1
# remaining ele in both arr
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

my_arr = [1,5,2,3,6,8733,0,23,55555]
print(mergeSort(my_arr,0,len(my_arr) - 1))

    

    