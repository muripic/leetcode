###############
# Description #
###############

# Difficulty: medium

# Given a string s, find the length of the longest substring
# without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence
# and not a substring.

# Constraints:
#     0 <= s.length <= 5 * 104
#     s consists of English letters, digits, symbols and spaces.


############
# Solution #
############


def length_of_longest_substring(s: str) -> int:
    # Store the longest substring so far
    longest = 0
    # Start of the current substring
    start = 0
    lookup = dict()  # key: char, value: last position
    for i, char in enumerate(s):
        last_pos = lookup.get(char)
        if last_pos is not None:
            longest = max(longest, i - start)
            # Start again after the repeated item,
            # if it's larger than last start
            start = max(start, last_pos + 1)
        lookup[char] = i
    # Also consider the substring from the last start to
    # the end of the array
    longest = max(longest, len(s) - start)
    return longest


# Official solution:
# https://leetcode.com/problems/longest-substring-without-repeating-characters/solutions/127839/longest-substring-without-repeating-characters


#########
# Tests #
#########

assert length_of_longest_substring("abcabcbb") == 3

assert length_of_longest_substring("bbbbb") == 1

assert length_of_longest_substring("pwwkew") == 3

assert length_of_longest_substring("") == 0

assert length_of_longest_substring("ab") == 2

assert length_of_longest_substring("a") == 1

assert length_of_longest_substring("abba") == 2

print("All tests passed :)")
