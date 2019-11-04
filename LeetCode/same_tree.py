# Given two binary trees, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
'''
Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorder(self, p):
        result = []
        if p:
            result.append(self.inorder(p.left))
            result.append(p.val)
            result.append(self.inorder(p.right))
        return result

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if self.inorder(p) == self.inorder(q):
            return True
        else:
            return False

p = TreeNode(1)
p.left = TreeNode(2)
# p.right = TreeNode(1)
q = TreeNode(1)
# q.left = TreeNode(1)
q.right = TreeNode(1)
s = Solution()
print(s.inorder(p))
print(s.inorder(q))
print(s.isSameTree(p, q))
'''
[[[], 2, []], 1, [[], 1, []]]
[[[], 1, []], 1, [[], 1, []]]
False
'''

p = TreeNode(1)
p.left = TreeNode(2)
# p.right = TreeNode(1)
q = TreeNode(1)
# q.left = TreeNode(1)
q.right = TreeNode(1)
s = Solution()
print(s.inorder(p))
print(s.inorder(q))
print(s.isSameTree(p, q))
'''
[[[], 2, []], 1, []]
[[], 1, [[], 1, []]]
False
'''

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(1)
q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(1)
s = Solution()
print(s.inorder(p))
print(s.inorder(q))
print(s.isSameTree(p, q))
'''
[[[], 2, []], 1, [[], 1, []]]
[[[], 2, []], 1, [[], 1, []]]
True
'''