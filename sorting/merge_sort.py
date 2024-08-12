def merge(arr, start, mid, end):
    """
    We need to take two pointers.
    first pointer will point to first slice first element and go till mid
    second pointer will point to second slice first element and go till end
    """
    first_pointer = start
    second_pointer = mid + 1
    temp_array = []
    while (first_pointer <= mid) and (second_pointer <= end):
        if arr[first_pointer] < arr[second_pointer]:
            temp_array.append(arr[first_pointer])
            first_pointer += 1
        else:
            temp_array.append(arr[second_pointer])
            second_pointer += 1

    while first_pointer <= mid:
        temp_array.append(arr[first_pointer])
        first_pointer += 1

    while second_pointer <= end:
        temp_array.append(arr[second_pointer])
        second_pointer += 1
    
    #  Copy temp array elements from start to end position in original array start to end
    for i in range(start, end + 1):
        arr[i] = temp_array[i-start]


def merge_sort(arr, start, end):
    if start >= end:
        return
    # Calculating MID
    mid = start + (end - start) // 2
    # First part will start from 0 to mid
    merge_sort(arr, start, mid)
    # Next part will start from mid+1 to len(arr)-1
    merge_sort(arr, mid + 1, end)
    # Merge both parts using temp array
    merge(arr, start, mid, end)


arr = [1,2,3,4]
start = 0
end = len(arr) - 1
merge_sort(arr=arr, start=start, end=end)
print(arr)
