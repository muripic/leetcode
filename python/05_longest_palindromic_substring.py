###############
# Description #
###############

# Difficulty: medium

# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"

# Constraints:
#     1 <= s.length <= 1000
#     s consist of only digits and English letters.


############
# Solution #
############


# O(n2) solution:
# - Traverse the string.
# - Taking each character as the center, expand indices to the left and right
#   to get the longest palindrome for that char as the center.
# - Consider two cases: odd length and even length palindromes (for even length,
#   item will be one of the two center items).
def longest_palindrome(s: str) -> str:
    res = ""
    for i in range(len(s)):
        # Odd length case
        l = i
        r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            curr_len = r - l + 1
            if curr_len > len(res):
                res = s[l : r + 1]
            l -= 1
            r += 1
        # Even length case (same as before but with r starting on i + 1)
        l = i
        r = i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            curr_len = r - l + 1
            if curr_len > len(res):
                res = s[l : r + 1]
            l -= 1
            r += 1
    return res


#########
# Tests #
#########

assert longest_palindrome("babad") in ["bab", "aba"]
assert longest_palindrome("cbbd") == "bb"

print("All tests passed :)")
