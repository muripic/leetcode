###############
# Description #
###############

# https://leetcode.com/problems/find-center-of-star-graph/

# Difficulty: easy

# There is an undirected star graph consisting of n nodes labeled from 1 to n.
# A star graph is a graph where there is one center node and exactly n - 1 edges
# that connect the center node with every other node.

# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates
# that there is an edge between the nodes ui and vi. Return the center of the given
# star graph.

# Example 1:

#     1
#     |
#     2
#    / \
#   3   4

# Input: edges = [[1,2],[2,3],[4,2]]
# Output: 2
# Explanation: As shown in the figure above, node 2 is connected to every other node,
# so 2 is the center.

# Example 2:

# Input: edges = [[1,2],[5,1],[1,3],[1,4]]
# Output: 1


############
# Solution #
############

from typing import List


def find_center(edges: List[List[int]]) -> int:
    # Find the element repeated in the first two edges
    return set(edges[0]).intersection(set(edges[1])).pop()


#########
# Tests #
#########

assert find_center([[1, 2], [2, 3], [4, 2]]) == 2
assert find_center([[1, 2], [5, 1], [1, 3], [1, 4]]) == 1

print("All tests passed :)")
