###############
# Description #
###############

# Difficulty: easy

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two ones added together.
# 12 is written as XII, which is simply X + II.
# The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:

#     I can be placed before V (5) and X (10) to make 4 and 9.
#     X can be placed before L (50) and C (100) to make 40 and 90.
#     C can be placed before D (500) and M (1000) to make 400 and 900.

# Given a roman numeral, convert it to an integer.

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Constraints:

#     1 <= s.length <= 15
#     s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
#     It is guaranteed that s is a valid roman numeral in the range [1, 3999].


############
# Solution #
############

VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_int(s: str) -> int:
    res = 0
    i = 0
    while i < len(s):
        if i == len(s) - 1 or VALUES[s[i]] >= VALUES[s[i + 1]]:
            res += VALUES[s[i]]
            i += 1
        else:
            res += VALUES[s[i + 1]] - VALUES[s[i]]
            i += 2
    return res


# 1. Iteration (looking forward):
#
# Traverse all the characters in the roman numeral.
# In some cases we move forward only one position:
# 1. If there is only one character or it's the last one, convert the value to
# decimal and sum it to the result.
# 2. If the next value is lower or the same, also convert value and sum it.
# The other case is the substraction one:
# In that case, the next value is larger than the current one. We calculate the
# subtraction and move forward two positions.
# Time complexity: O(n)

#########################
# Alternative solutions #
#########################

# 2. Replacing the substraction case:


def roman_to_int_str_rep(s: str) -> int:
    s = (
        s.replace("IV", "IIII")
        .replace("IX", "VIIII")
        .replace("XL", "XXXX")
        .replace("XC", "LXXXX")
        .replace("CD", "CCCC")
        .replace("CM", "DCCCC")
    )
    return sum(map(lambda x: VALUES[x], s))


# 3. Iteration (looking back):
#
# Check if the current character has a greater value than the previous character.
# If so, add the current character value minus twice the previous character value
# to the 'res' variable. This is because the previous character value was added once
# already and needs to be subtracted to get the correct value.
# If the current character does not have a greater value than the previous character,
# add the current character value to the 'res' variable.


def roman_to_int_substraction(s: str) -> int:
    res = 0
    for i in range(len(s)):
        if i > 0 and VALUES[s[i]] > VALUES[s[i - 1]]:
            res += VALUES[s[i]] - 2 * VALUES[s[i - 1]]
        else:
            res += VALUES[s[i]]
    return res


#########
# Tests #
#########

assert roman_to_int("III") == 3
assert roman_to_int("LVIII") == 58
assert roman_to_int("MCMXCIV") == 1994
print("All tests passed :)")
