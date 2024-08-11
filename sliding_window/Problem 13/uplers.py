import sys


def solution(A, k):
    previous_max_sum, previous_start, previous_end = 0, 0, 0
    window_start, window_sum = 0, None
    max_sum = -sys.maxsize
    for window_end in range(len(A)):
        if not window_sum:
            window_sum = A[window_end]
        else:
            window_sum += A[window_end]
        if window_end >= k-1:
            max_sum = max(window_sum, max_sum)
            if previous_max_sum < max_sum:
                previous_start = window_start
                previous_end = window_end
            window_sum -= A[window_start]
            window_start += 1
            previous_max_sum = max_sum
    return max_sum, previous_start, previous_end


array = [6, 1, 4, 6, 3, 2, 7, 4]
K = 3
L = 2
sum1, start1, end1 = solution(array, K)
# print(sum1, start1, end1)
sum2, start2, end2 = solution(array, L)
# print(sum2, start2, end2)

first_set = set(range(start1, end1+1))
second_set = set(range(start2, end2+1))
if len(first_set.intersection(second_set)) == 0:
    print(sum1+sum2)
else:
    print(-1)

