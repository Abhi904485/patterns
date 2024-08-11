def reverse_array_using_recursion(arr):
    if len(arr) == 1:
        return arr
    return reverse_array_using_recursion(arr[1:])+ arr[0:1]

def reverse_array_using_swap(arr):
    n= len(arr)
    for i in range(len(arr)//2):
        arr[i] , arr[n-i-1] = arr[n-i-1], arr[i]
    return arr
    
def reverse_array_using_built_in_array(arr: list):
    arr.reverse()
    return arr

def reverse_array_using_builtin(arr: list):
    return list(reversed(arr))

def reverse_array_using_slice(arr):
    print(arr[::-1])



arr = [1,2,3,4,5]
print(reverse_array_using_recursion(arr=arr))
arr = [1,2,3,4,5]
print(reverse_array_using_swap(arr=arr))
arr = [1,2,3,4,5]
print(reverse_array_using_built_in_array(arr=arr))
arr = [1,2,3,4,5]
print(reverse_array_using_builtin(arr=arr))
arr = [1,2,3,4,5]
reverse_array_using_slice(arr=arr)
