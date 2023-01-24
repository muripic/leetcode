###############
# Description #
###############

# Difficulty: easy

# Given a sorted array of distinct integers and a target value, return the
# index if the target is found. If not, return the index where it would be
# if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

# Constraints:

#     1 <= nums.length <= 104
#     -104 <= nums[i] <= 104
#     nums contains distinct values sorted in ascending order.
#     -104 <= target <= 104


############
# Solution #
############

from typing import List

# Iterative solution


def search_insert(nums: List[int], target: int) -> int:
    start = 0
    end = len(nums)
    while start < end:
        mid = (end + start) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            end = mid
        else:  # if nums[mid] < target
            start = mid + 1
    return start


# Recursive solution is better suited just to check if an element exists.
# If we need to return the position, like here, we need to add start and end
# params to the recursive call.

#########
# Tests #
#########

# Arrays of even length
even_nums = [1, 3, 5, 6]
assert search_insert(even_nums, 5) == 2
assert search_insert(even_nums, 2) == 1
assert search_insert(even_nums, 7) == 4
assert search_insert(even_nums, -2) == 0

# # Arrays of odd length
odd_nums = [1, 3, 4, 5, 6]
assert search_insert(odd_nums, 5) == 3
assert search_insert(odd_nums, 2) == 1
assert search_insert(odd_nums, 7) == 5
assert search_insert(odd_nums, -2) == 0

# # Only one element
only_one_nums = [1]
assert search_insert(only_one_nums, 1) == 0
assert search_insert(only_one_nums, -1) == 0
assert search_insert(only_one_nums, 2) == 1

print("All tests passed :)")
