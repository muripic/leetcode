###############
# Description #
###############

# Difficulty: easy

# Given an integer array nums sorted in non-decreasing order, remove
# the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result.
# It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying
# the input array in-place with O(1) extra memory.

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }

# If all assertions pass, then your solution will be accepted.

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two
# elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k.

# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five
# elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k.

# Constraints:

#     1 <= nums.length <= 3 * 104
#     -100 <= nums[i] <= 100
#     nums is sorted in non-decreasing order.


############
# Solution #
############

from typing import List

# The first index updates the value in our input array while reading
# the data from the second index.
# First Index is responsible for writing unique values in our input array,
# while Second Index will read the input array and pass all the distinct
# elements to First Index.
# Move second index until the two numbers are different. Then, update the
# first repeated number from the beginning of the array with the new one.


def remove_duplicates(nums: List[int]) -> int:
    if len(nums) == 1:
        return 1
    i = 0  # index to update value
    # j reads the data.
    # Keep moving j forward until the first different number.
    for j in range(1, len(nums)):
        # If the two numbers are different, move i one position
        # # forward, and assign the value of the j index.
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1


# Official solution:
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/solutions/2601915/remove-duplicates-from-sorted-array/


#########
# Tests #
#########

# Test setup
nums_1 = [1, 1, 2]
expected_nums_1 = [1, 2]
res = remove_duplicates(nums_1)

# Asserts
assert res == 2
for i in range(res):
    assert nums_1[i] == expected_nums_1[i]

# Test setup
nums_2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
expected_nums_2 = [0, 1, 2, 3, 4]
res = remove_duplicates(nums_2)

# Asserts
assert res == 5
for i in range(res):
    assert nums_2[i] == expected_nums_2[i]

# Test setup
nums_3 = [1, 1]
expected_nums_3 = [1]
res = remove_duplicates(nums_3)

# Asserts
assert res == 1
for i in range(res):
    assert nums_3[i] == expected_nums_3[i]

print("All tests passed :)")
