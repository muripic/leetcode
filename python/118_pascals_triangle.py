###############
# Description #
###############

# Difficulty: easy

# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it:
#
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:

# Input: numRows = 1
# Output: [[1]]

# Constraints:
#     1 <= numRows <= 30


############
# Solution #
############

from typing import List


def generate(num_rows: int) -> List[List[int]]:
    # Build a triangle full of 1s
    res = [[1] * (i + 1) for i in range(num_rows)]
    # First rows are always [1] and [1, 1], so we start at 2
    for i in range(2, num_rows):
        prev_row = res[i - 1]
        curr_row = res[i]
        # Fill the middle of the current row with the
        # sums of the previous row
        for j in range(1, len(curr_row) - 1):
            curr_row[j] = prev_row[j - 1] + prev_row[j]
    return res


#########
# Tests #
#########

assert generate(1) == [[1]]
assert generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

print("All tests passed :)")
