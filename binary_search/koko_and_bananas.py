from typing import List
from math import ceil
piles = [30,11,23,4,20]
total_time = 6


def check_speed(speed, piles, total_time):
    for i in piles:
        total_time -= ceil(i/speed)
        if total_time < 0:
            return False
    else:
        if total_time >0:
            return False
        elif total_time == 0:
            return True

def check_speed_optimized(speed, piles, total_time):
    time = 0
    for i in piles:
        time += ceil(i/speed)
    if time <= total_time:
        return True
    else:
        return False
        
# Brute Force Approach
def minEatingSpeedBruteForce(piles: List[int], total_time: int) -> int:
    left = 1
    right = max(piles)
    for speed in range(left, right+1):
        if check_speed(speed=speed, piles=piles, total_time=total_time):
            return speed
        else:
            continue
    else:
        return 0


def minEatingSpeedOptimized(piles, total_time: int) -> int:
    min_speed = 1
    max_speed = max(piles)
    while min_speed < max_speed:
        current_speed  = min_speed + (max_speed- min_speed)//2
        if check_speed_optimized(speed=current_speed, piles=piles, total_time=total_time):
            max_speed = current_speed
        else:
            min_speed = current_speed + 1
    return max_speed
            
# print(minEatingSpeedBruteForce(piles, total_time))
print(minEatingSpeedOptimized(piles, total_time))
        
