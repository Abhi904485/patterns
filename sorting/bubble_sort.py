def bubble_sort(arr):
    for i in range(len(arr) - 1, -1, -1):
        max_so_far, index = arr[i], i
        for j in range(i - 1, -1, -1):
            if max_so_far < arr[j]:
                max_so_far, index = arr[j], j
        arr[i] , arr[index] = arr[index], arr[i]
    return arr


arr = [4, 3, 2, 1]
print(bubble_sort(arr=arr))
