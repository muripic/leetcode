###############
# Description #
###############

# Difficulty: easy

# Given an array of integers nums and an integer target, return indices
# of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:

#     2 <= nums.length <= 104
#     -109 <= nums[i] <= 109
#     -109 <= target <= 109
#     Only one valid answer exists.

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


############
# Solution #
############

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    values = dict()
    for i in range(len(nums)):
        value_index = values.get(target - nums[i])
        if value_index is not None:
            return [value_index, i]
        values[nums[i]] = i


# Possible solutions and explanation
# 1. Brute force: checking every number against all the other numbers in the array.
# This would require two nested loops -> O(n2)
# 2. Hash and substraction: create a hash with the values as keys and the
# index as values. By substracting the current value from the target, we will know
# which other number is necessary for the sum, so we can look it up in the hash table,
# get its index, and the answer will be the current index and the index found in the
# hash table.


#########
# Tests #
#########

assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
assert two_sum([3, 3], 6) == [0, 1]
print("All tests passed :)")
