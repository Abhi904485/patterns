def selection_sort(arr):
    for i in range(len(arr)):
        min_so_far, index = arr[i], i
        for j in range(i+1, len(arr)):
            if min_so_far > arr[j]:
                min_so_far, index = arr[j], j
        arr[i] , arr[index] = arr[index], arr[i]
    return arr


arr = [4, 1, 3, 2]
print(selection_sort(arr=arr))
