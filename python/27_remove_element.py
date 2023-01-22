###############
# Description #
###############

# Difficulty: easy

# Given an integer array nums and an integer val, remove all occurrences of
# val in nums in-place. The relative order of the elements may be changed.

# Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result.
# It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying
# the input array in-place with O(1) extra memory.

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.

# int k = removeElement(nums, val); // Calls your implementation

# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }

# If all assertions pass, then your solution will be accepted.

# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements
# of nums being 2.
# It does not matter what you leave beyond the returned k.

# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements
# of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k.

# Constraints:

#     0 <= nums.length <= 100
#     0 <= nums[i] <= 50
#     0 <= val <= 100


############
# Solution #
############

from typing import List


def remove_element(nums: List[int], val: int) -> int:
    i = 0
    j = len(nums)
    while i < j:
        if nums[i] == val:
            j -= 1
            nums[i] = nums[j]
        else:
            i += 1
    return j


# Official solution
# https://leetcode.com/problems/remove-element/solutions/127824/remove-element/
# https://www.youtube.com/watch?v=Pcd1ii9P9ZI

#########
# Tests #
#########

# Test setup
nums_1 = [3, 2, 2, 3]
expected_nums_1 = [2, 2]
res = remove_element(nums_1, 3)

# Asserts
assert res == 2
assert set(nums_1[0:res]) == set(expected_nums_1)

# Test setup
nums_2 = [0, 1, 2, 2, 3, 0, 4, 2]
expected_nums_2 = [0, 1, 4, 0, 3]
res = remove_element(nums_2, 2)

# Asserts
assert res == 5
assert set(nums_2[0:res]) == set(expected_nums_2)

# Test setup
nums_3 = []
expected_nums_3 = []
res = remove_element(nums_3, 0)

# Asserts
assert res == 0
assert set(nums_3[0:res]) == set(expected_nums_3)

# Test setup
nums_4 = [2]
expected_nums_4 = [2]
res = remove_element(nums_4, 3)

# Asserts
assert res == 1
assert set(nums_4[0:res]) == set(expected_nums_4)

# Test setup
nums_5 = [3, 3]
expected_nums_5 = []
res = remove_element(nums_5, 3)

# Asserts
assert res == 0
assert set(nums_5[0:res]) == set(expected_nums_5)

print("All tests passed :)")
