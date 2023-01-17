###############
# Description #
###############

# Difficulty: easy

# Write a function to find the longest common prefix string amongst
# an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower", "flow", "flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog", "racecar", "car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:

#     1 <= strs.length <= 200
#     0 <= strs[i].length <= 200
#     strs[i] consists of only lowercase English letters.


############
# Solution #
############

from typing import List


def longest_common_prefix(self, strs: List[str]) -> str:
    pass


#########
# Tests #
#########

assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_common_prefix(["dog", "racecar", "car"]) == ""
print("All tests passed :)")
