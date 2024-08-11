def insertion_sort(arr):
    for i in range(1, len(arr)):
        while i>0 and arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -=1
    return arr


arr = [3, 4, 2, 1]
print(insertion_sort(arr=arr))