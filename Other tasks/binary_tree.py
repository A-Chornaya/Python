# Binary Tree

class Node:
    def __init__(self, value):
        self.value= value
        self.left = None
        self.right = None

    def add_childs(self, left, right):
        self.left = left
        self.right = right

    def add_left(self, left):
        self.left = left

    def add_right(self, right):
        self.right = right


class BinaryTree():
    def __init__(self):
        # super(BinaryTree, self).__init__(value)
        self.root = None

    def add_element(self, elem):
        if self.root is None:
            self.root = Node(elem)
        else:
            self._add_new_child(self.root, elem)

    def _add_new_child(self, node, value):
        if value <= node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_new_child(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_new_child(node.right, value)

    def print(self, order='inorder'):
        if self.root is not None:
            if order == 'inorder':
                self._print_inorder(self.root)
            elif order == 'preorder':
                self._print_preorder(self.root)
            elif order == 'postorder':
                self._print_postorder(self.root)
            elif order == 'breadth':
                self._breadth_first()


    def _print_inorder(self, node):
        if node is not None:
            self._print_inorder(node.left)
            print(str(node.value))
            self._print_inorder(node.right)

    def _print_preorder(self, node):
        if node is not None:
            print(str(node.value))
            self._print_preorder(node.left)
            self._print_preorder(node.right)

    def _print_postorder(self, node):
        if node is not None:
            self._print_postorder(node.left)
            self._print_postorder(node.right)
            print(str(node.value))

    def _breadth_first(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            temp_node = queue.pop(0)
            print(temp_node.value)
            if temp_node.left is not None:
                queue.append(temp_node.left)
            if temp_node.right is not None:
                queue.append(temp_node.right)



tree = BinaryTree()
tree.add_element(10)
tree.add_element(5)
tree.add_element(15)
tree.add_element(4)
tree.add_element(20)
tree.add_element(7)
print('depth first - inorder')
tree.print()
print('*****************')
print('depth first - preorder')
tree.print(order='preorder')
print('*****************')
print('depth first - postorder')
tree.print(order='postorder')
print('*****************')
print('breadth first')
tree.print(order='breadth')

'''
Result

depth first - inorder
4
5
7
10
15
20
*****************
depth first - preorder
10
5
4
7
15
20
*****************
depth first - postorder
4
7
5
20
15
10
*****************
breadth first
10
5
15
4
7
20
'''