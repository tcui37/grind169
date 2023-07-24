"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None: return None

        def clone(node,copy=None):
            if copy == None:
                copy = {node: Node(node.val)}
            for neighbor in node.neighbors:
                if neighbor not in copy:
                    copy[neighbor] = Node(neighbor.val)
                    clone(neighbor,copy)

                copy[node].neighbors.append(copy[neighbor])
   
            return copy[node]

        return clone(node)
    