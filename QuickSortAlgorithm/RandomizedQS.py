# Python code for Quick sort Algorithm
import random

def partition(arr, p, r):
    in_num= random.randint(0,len(arr))
    pivot= arr[in_num]
    arr[0], arr[in_num] = arr[in_num], arr[0]
    i = p
    for j in range(p+1, r+1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[p], arr[i] = arr[i], arr[p]
    return i

def quickSort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quickSort(arr, p, q-1)
        quickSort(arr, q+1, r)

# Driver Code
arr= eval(input()) # Give input in a list
quickSort(arr, 0, len(arr)-1)
print(arr) 

'''
TC : Worst case & Best case [O(nlogn)]
SC : O(1)
'''