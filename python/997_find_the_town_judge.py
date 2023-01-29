###############
# Description #
###############

# https://leetcode.com/problems/find-the-town-judge/

# Difficulty: easy

# In a town, there are n people labeled from 1 to n.
# There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

#     The town judge trusts nobody.
#     Everybody (except for the town judge) trusts the town judge.
#     There is exactly one person that satisfies properties 1 and 2.

# You are given an array trust where trust[i] = [ai, bi] representing that
# the person labeled ai trusts the person labeled bi. If a trust relationship
# does not exist in trust array, then such a trust relationship does not exist.

# Return the label of the town judge if the town judge exists and can be identified,
# or return -1 otherwise.

# Example 1:

# Input: n = 2, trust = [[1,2]]
# Output: 2

# Example 2:

# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3

# Example 3:

# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1


############
# Solution #
############

from typing import List

# Solution 1: brute force, representing the graph as an adjacency matrix


def find_judge_matrix(n: int, trust: List[List[int]]) -> int:
    # Build graph as adjacency matrix
    graph = [[0] * n for _ in range(n)]
    for rel in trust:
        graph[rel[0] - 1][rel[1] - 1] = 1
    for person in range(n):
        # Trusts nobody: row is all 0
        trusts_nobody = sum(graph[person]) == 0
        # Is trusted by everyone: col is all 1 except for one (itself)
        is_trusted = sum(graph[row][person] for row in range(n)) == n - 1
        if trusts_nobody and is_trusted:
            return person + 1
    return -1


# Complexity: time O(n2) and space O(n2).

# Solution 2:
# Keep track of the cumulative score of each person: if person A
# trusts person B, we decrement A's score and increment B's score
# The judge is the only person that ends up with a score of N-1.


def find_judge(n: int, trust: List[List[int]]) -> int:
    trust_scores = [0] * n
    for truster, trusted in trust:
        trust_scores[truster - 1] -= 1
        trust_scores[trusted - 1] += 1
    for person, score in enumerate(trust_scores):
        if score == n - 1:
            return person + 1
    return -1


# Complexity: O(n + t) where t is len(trust) (edges)

#########
# Tests #
#########

assert find_judge(2, [[1, 2]]) == 2
assert find_judge(3, [[1, 3], [2, 3]]) == 3
assert find_judge(3, [[1, 3], [2, 3], [3, 1]]) == -1

print("All tests passed :)")
