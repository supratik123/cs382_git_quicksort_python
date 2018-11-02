#!/usr/bin/python3
from quicksort import *

if __name__ == '__main__':
    arr = [1, 2, 3, 50, 45, 40, 20, 25, 35, 30, 28]
    quickSort(arr, 0, len(arr)-1)
    print("Sorted array is:")
    for n in arr[:-1]: print(str(n), end=', ')
    print(arr[-1])
