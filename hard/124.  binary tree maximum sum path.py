# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # use both children
        memo = {}
        def treePath(node):
            if node is None: return -float('inf')
            leftP = nodePath(node.left)
            rightP = nodePath(node.right)
            case1 = max(node.val + leftP + rightP,node.val)
            case2 = max(treePath(node.left),treePath(node.right))
            case3 = node.val + max(leftP,rightP)
            return max(case1,case2,case3)
        def nodePath(node):
            if node is None: return -float('inf')
            if node in memo: return memo[node]
            leftP = nodePath(node.left)
            rightP = nodePath(node.right)
            memo[node] = max(node.val,node.val+leftP,node.val + rightP)
            return memo[node]
        return max(treePath(root),nodePath(root))
