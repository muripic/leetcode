###############
# Description #
###############

# Difficulty: easy

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# An input string is valid if:
# - Open brackets must be closed by the same type of brackets.
# - Open brackets must be closed in the correct order.
# - Every close bracket has a corresponding open bracket of the same type.

# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

# Example 3:

# Input: s = "(]"
# Output: false

# Constraints:

#     1 <= s.length <= 104
#     s consists of parentheses only '()[]{}'.


############
# Solution #
############

BRACKETS = {")": "(", "]": "[", "}": "{"}


def is_valid(s: str) -> bool:
    stack = []
    for elem in s:
        if elem in "([{":
            stack.append(elem)
        elif not stack:
            return False
        else:
            if BRACKETS[elem] != stack.pop():
                return False
    return len(stack) == 0


#########
# Tests #
#########

assert is_valid("()") == True
assert is_valid("()[]{}") == True
assert is_valid("(]") == False
assert is_valid("([])({}") == False
assert is_valid("([{}])") == True
assert is_valid("]") == False
print("All tests passed :)")
