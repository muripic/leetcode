###############
# Description #
###############

# https://leetcode.com/problems/find-if-path-exists-in-graph/

# Difficulty: easy

# There is a bi-directional graph with n vertices, where each vertex is
# labeled from 0 to n - 1 (inclusive). The edges in the graph are represented
# as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a
# bi-directional edge between vertex ui and vertex vi. Every vertex pair
# is connected by at most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists from vertex
# source to vertex destination.

# Given edges and the integers n, source, and destination, return true if
# there is a valid path from source to destination, or false otherwise.

# Example 1:

# Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2

# Example 2:

# Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]],
# source = 0, destination = 5
# Output: false
# Explanation: There is no path from vertex 0 to vertex 5.

# Constraints:

#     1 <= n <= 2 * 105
#     0 <= edges.length <= 2 * 105
#     edges[i].length == 2
#     0 <= ui, vi <= n - 1
#     ui != vi
#     0 <= source, destination <= n - 1
#     There are no duplicate edges.
#     There are no self edges.


############
# Solution #
############

from typing import List
from collections import defaultdict


def valid_path(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    # Build graph from edges
    graph = defaultdict(list)
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)

    # Keep track of visited nodes
    visited = [False] * n

    # Start from source
    queue = [source]
    visited[source] = True

    # BFS
    while queue:
        curr = queue.pop()

        if curr == destination:
            return True

        for neighbour in graph[curr]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)
    return False


# Official solution:
# https://leetcode.com/problems/find-if-path-exists-in-graph/solutions/2715942/find-if-path-exists-in-graph/


#########
# Tests #
#########

assert valid_path(3, [[0, 1], [1, 2], [2, 0]], 0, 2) == True
assert valid_path(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5) == False

print("All tests passed :)")
