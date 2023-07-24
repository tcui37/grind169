# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodNodeHelp(root,cur_max):
            leftGood,rightGood = 0,0
            if root.left: leftGood = 1 + goodNodeHelp(root.left,root.left.val) if root.left.val >= cur_max else goodNodeHelp(root.left,cur_max) 
            if root.right: rightGood = 1 + goodNodeHelp(root.right,root.right.val) if root.right.val >= cur_max else goodNodeHelp(root.right,cur_max)
            return leftGood + rightGood
        return 1 + goodNodeHelp(root,root.val)
            

            
