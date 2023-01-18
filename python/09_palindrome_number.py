###############
# Description #
###############

# Difficulty: easy

# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Constraints:

#     -231 <= x <= 231 - 1

# Follow up: Could you solve it without converting the integer to a string?


############
# Solution #
############


def is_palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]


def is_palindrome_no_str(x: int) -> bool:
    if x < 0:
        return False
    original = x
    reversed = 0
    while original != 0:
        digit = original % 10
        reversed = reversed * 10 + digit
        original = original // 10
    return x == reversed


# Official solution
# https://leetcode.com/problems/palindrome-number/solutions/127661/palindrome-number/


def is_palindrome_no_str_half(x: int) -> bool:
    # Special cases:
    # When x < 0, x is not a palindrome.
    # Also if the last digit of the number is 0, the first digit
    # also needs to be 0. Only 0 satisfoes this property.
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reversed = 0
    # Since we divided the number by 10, and multiplied the reversed
    # number by 10, when the original number is less than the reversed,
    # it means we've processed half of the number digits.
    while x > reversed:
        digit = x % 10
        reversed = reversed * 10 + digit
        x = x // 10
    # When the length is an odd number, we can get rid of the middle digit.
    # For example when the input is 12321, at the end of the while loop
    # we get x = 12, revertedNumber = 123.
    return x == reversed or x == reversed // 10


#########
# Tests #
#########

assert is_palindrome(121) == True
assert is_palindrome(-121) == False
assert is_palindrome(10) == False

assert is_palindrome_no_str(121) == True
assert is_palindrome_no_str(-121) == False
assert is_palindrome_no_str(10) == False

print("All tests passed :)")
