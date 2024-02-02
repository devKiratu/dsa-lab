"""
Given an integer n , reverse it and return the reversed integer.

# example
input = 12345
output = 54321

Constraints:
    - n >= 0
"""

def reverse_number(n: int) -> int:
    if n == 0:
        return n
    base = 10
    result = 0

    # extract digits
    while n > 0:
        digit = n % base
        n = n // base
        result = (result * base) + digit
    
    return result

"""
Analysis:

Time Complexity:
    - the loop runs n times where n is the number of digits in the input.
    This gives O(n)

Space Complexity:
    - the algorithm uses O(1) space to store varibles and result
"""

if __name__ == '__main__':
    num = 12345
    print(f" {num} reversed is {reverse_number(num)}")
    num = 0
    print(f" {num} reversed is {reverse_number(num)}")
    num = 65894258
    print(f" {num} reversed is {reverse_number(num)}")
