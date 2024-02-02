"""
Given a sorted list of numbers s, and a target, return a list of 3
numbers that add up to the target
"""
from typing import List

def three_numbers(s: List[int], target: int) -> List[int]:
    i  = 0
    while i < len(s):
        left = i + 1
        right = len(s) - 1
        while left < right:
            total = s[i] + s[left] + s[right]
            if total == target:
                return [s[i], s[left], s[right]]
            elif total < target:
                left += 1
            else:
                right -= 1
        i += 1

"""
Analysis:

Time Complexity:
    - for every number (n) in the list, we iterate over a subset (k) of the
    list k/2 times. 
    This makes the total complexity to be (n * k/2) where k is (n - i + 1)
    This makes it O(n^2)

Space Complexity:
    - This algorithm uses O(1) space for storing the variables used in the calculations

"""


if __name__ == '__main__':
    print(three_numbers([1, 2, 3, 4, 5, 6, 7, 8 ], 16))
