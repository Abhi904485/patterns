# From Card we can take k cards from left or right in consecutive order. 
# Find the maximum point we can obtain from the cards.

cards = [9,7,7,9,7,7,9]
k = 7


def max_point(cards, k):
    max_sum = 0
    max_sum_so_far = 0
    for point_index in range(k):
        max_sum += cards[point_index]
        max_sum_so_far = max(max_sum_so_far, max_sum)
    right_point_index = len(cards) - 1
    for reverse_point_index in range(k-1, -1, -1):
        max_sum -= cards[reverse_point_index]
        max_sum += cards[right_point_index]
        max_sum_so_far = max(max_sum_so_far, max_sum)
        right_point_index -= 1
        
    return max_sum_so_far
    

print(max_point(cards, k))


