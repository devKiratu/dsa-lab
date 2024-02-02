"""
Given two integers a and b, return a tuple containing the quotient
and remainder of the division operation. If there is no remainder,
put zero in its place

# example
divide(6, 3) # (2, 0)

# terms:
# dividend - the number that is being divided
# divisor - the number doing the dividing
# remainder - what is left over, if anything, after dividing 

You must not use the division operator
"""
from typing import Tuple

def divide(a: int, b: int) -> Tuple[int, int]:
    if b == 0:
        raise ZeroDivisionError
    quotient = 0
    while a >= b:
        a -= b
        quotient += 1
    if a == 0:
        return (quotient, 0)
    return (quotient, a)

"""
Analysis:

Time Complexity:
    - the division loop runs n/q times where n is the input and q 
    is the quotient. In a worst case if q is 1, the loop runs n times
    Thus time complexity is O(n)

Space Complexity:
    - the algorithm uses O(1) space to store variables and output
"""


if __name__ == '__main__':
    print(f"6 / 3 = {divide(6, 3)}")
    print(f"7 / 2 = {divide(7, 2)}")
    print(f"10 / 3 = {divide(10, 3)}")
    print(f"10 / 0 = {divide(10, 0)}")
