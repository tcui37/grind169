# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if root is None:
            return "None,"
        return (
            str(root.val) + "," + self.serialize(root.left) + self.serialize(root.right)
        )

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        # i couldnt get this part too work without the jank access to parent memory trick >.< this part is from the official solution
        def rdeserialize(l):
            if l[0] == "None":
                l.pop(0)
                return None
            root = TreeNode(l[0])
            l.pop(0)
            root.left, root.right = rdeserialize(l), rdeserialize(l)
            return root

        data_list = data.split(",")
        root = rdeserialize(data_list)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
