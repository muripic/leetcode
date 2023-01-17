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


def longest_common_prefix(strs: List[str]) -> str:
    prefix = ""
    for i in range(len(min(strs))):
        letter = strs[0][i]
        for s in strs:
            if s[i] != letter:
                return prefix
        prefix += letter
    return prefix


# n = array length
# m = word length
# Complexity: O(n*m)

# Alternative solutions in https://leetcode.com/problems/longest-common-prefix/solutions/127449/longest-common-prefix/


#########
# Tests #
#########

assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_common_prefix(["dog", "racecar", "car"]) == ""
assert longest_common_prefix(["", "blabla", "bla", "blu"]) == ""
print("All tests passed :)")
