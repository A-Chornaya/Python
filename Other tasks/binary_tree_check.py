
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        result = self._inorder_check(root)
        return True if result != 'flag_False' else False

    def _inorder_check(self, current):
        result_left = self._inorder_check(current.left) if current.left is not None else []
        result_right = self._inorder_check(current.right) if current.right is not None else []

        if result_left == 'flag_False' or result_right == 'flag_False':
            return 'flag_False'

        result = self._current_check(current, result_left, result_right)
        if result:
            together = [current.val]
            together.extend(result_left)
            together.extend(result_right)
            return together
        else:
            return 'flag_False'

    def _current_check(self, current, left, right):
        if not all(list(map(lambda x: x < current.val, left))):
            return False
        if not all(list(map(lambda x: x > current.val, right))):
            return False
        return True

c = Solution()
t = TreeNode(5)
t.left = TreeNode(1)
# t.left.left = TreeNode(0)
t.left.right = TreeNode(2)
t.right = TreeNode(7)
t.right.left = TreeNode(6)
# t.right.right = TreeNode(8)
# t = []
print(c.isValidBST(t))



####################
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        result = self._inorder_check(root)
        return True if result != 'flag_False' else False

    def _inorder_check(self, current):
        result_left = self._inorder_check(current.left) if current.left is not None else []
        result_right = self._inorder_check(current.right) if current.right is not None else []

        if result_left == 'flag_False' or result_right == 'flag_False':
            return 'flag_False'

        left_check = self._left_check(current, result_left) if result_left else True
        right_check = self._right_check(current, result_right) if result_right else True

        if left_check and right_check:
            together = [current.val]
            together.extend(result_left)
            together.extend(result_right)
            return together
        else:
            return 'flag_False'

    def _left_check(self, current, left):
        if not all(list(map(lambda x: x < current.val, left))):
            return False
        return True

    def _right_check(self, current, right):
        if not all(list(map(lambda x: x > current.val, right))):
            return False
        return True

c = Solution()
t = TreeNode(5)
t.left = TreeNode(1)
# t.left.left = TreeNode(0)
t.left.right = TreeNode(2)
t.right = TreeNode(7)
t.right.left = TreeNode(6)
# t.right.right = TreeNode(8)
# t = []
print(c.isValidBST(t))      # True