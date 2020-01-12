'''
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = self._count_depth(root)

        return depth

    def _count_depth(self, node):
        if node is None:
            return 0
        return 1 + max(self._count_depth(node.left), self._count_depth(node.right))


# [3, 9, 20 ,null, null, 15, 7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

c = Solution()
tree_depth = c.maxDepth(root)
print(tree_depth)               # 3

# [3, 9, 20 ,null, null, 15, 7, 10]
root.right.right.left = TreeNode(10)
tree_depth2 = c.maxDepth(root)
print(tree_depth2)               # 4

# [1,2,null,3,null,4,null,5]
tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.left.left = TreeNode(3)
tree2.left.left.left = TreeNode(4)
tree2.left.left.left.left = TreeNode(5)
tree_depth3 = c.maxDepth(tree2)
print(tree_depth3)               # 5
