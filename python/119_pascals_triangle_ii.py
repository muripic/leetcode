###############
# Description #
###############

# Difficulty: easy

# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the
# Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it:
#
#       1
#      1 1
#     1 2 1
#    1 3 3 1
#   1 4 6 4 1

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]

# Example 2:

# Input: rowIndex = 0
# Output: [1]

# Example 3:

# Input: rowIndex = 1
# Output: [1,1]

# Constraints:
#     0 <= rowIndex <= 33

# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

############
# Solution #
############

from typing import List

# Solution 1: Generate all the rows until the required one


def get_row(row_index: int) -> List[int]:
    prev_row = [1]
    for i in range(1, row_index + 1):
        # Create array of needed length for new row
        curr_row = [1] * (i + 1)
        # Calculate new row based on previous one
        for j in range(1, len(curr_row) - 1):
            curr_row[j] = prev_row[j - 1] + prev_row[j]
        # Update previous row
        prev_row = curr_row
    return prev_row


# Solution 2: using formula


def factorial(n: int) -> int:
    res = 1
    for i in range(1, n + 1):
        res = res * i
    return res


def combinatorial(n: int, k: int) -> int:
    return factorial(n) // factorial(k) // factorial(n - k)


def get_row_with_formula(row_index: int) -> List[int]:
    # Create array of needed length for row
    res = [1] * (row_index + 1)
    for i in range(1, len(res) - 1):
        # Use combinatorial to generate row
        res[i] = combinatorial(row_index, i)
    return res


#########
# Tests #
#########

assert get_row(0) == [1]
assert get_row(1) == [1, 1]
assert get_row(3) == [1, 3, 3, 1]

import math

assert factorial(4) == math.factorial(4)
assert factorial(7) == math.factorial(7)
assert combinatorial(5, 3) == math.comb(5, 3)
assert combinatorial(8, 4) == math.comb(8, 4)

assert get_row_with_formula(0) == [1]
assert get_row_with_formula(1) == [1, 1]
assert get_row_with_formula(3) == [1, 3, 3, 1]

print("All tests passed :)")
