"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = defaultdict(list)
        copies = {}
        def clone(node):
            if node == None:
                return None

            if node in copies:
                return copies[node]

            else:
                root = Node(node.val)
                copies[node] = root

            for n in node.neighbors:
                if node in seen and n in seen[node]:
                    continue

                seen[node].append(n)
                neighbor = clone(n)
                if neighbor:
                    root.neighbors.append(neighbor)
            return root
        return clone(node)

        