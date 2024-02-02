"""
Given a sorted list of numbers s, and a target, return a list of 3
numbers that add up to the target. You can return the numbers in any order

Constraints:
    - Your solution must use O(n) time for the computation
"""
from typing import List, Dict, Tuple

def three_numbers(s: List[int], target: int) -> List[int]:
    ref: Dict[int, Tuple[int, int]] = {}
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] in ref:
            left, right = ref[s[i]]
            return [left, s[i], right]
        elif s[j] in ref:
            left, right = ref[s[j]]
            return [left, s[j], right]
        else:
            diff = target - (s[i] + s[j])
            ref[diff] = (s[i], s[j])
        i += 1
        j -= 1

"""
Analysis:

Time Complexity:
    - the algorithm checks for the possible combinations of three numbers in
    one iteration. This gives O(n)

Space Complexity:
    - This algorithm uses a dictionary to store the possible combinations that
    add up to the target. The dictionary grows with every iteration until a
    match is found. This results in O(n) space where n i the length of the
    input list

"""


if __name__ == '__main__':
    print(three_numbers([1, 2, 3, 4, 5, 6, 7, 8 ], 16))
