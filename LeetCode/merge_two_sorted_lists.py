'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2

        left = l1
        right = l2
        # create common_list
        if left.val <= right.val:
            common_list = ListNode(left.val)
            left = left.next
        else:
            common_list = ListNode(right.val)
            right = right.next
        common_pointer = common_list

        while left or right:
            if left and right:
                if left.val <= right.val:
                    common_pointer.next = ListNode(left.val)
                    left = left.next
                else:
                    common_pointer.next = ListNode(right.val)
                    right = right.next
            elif left:
                common_pointer.next = ListNode(left.val)
                left = left.next
            elif right:
                common_pointer.next = ListNode(right.val)
                right = right.next

            common_pointer = common_pointer.next

        return common_list

    @classmethod
    def print_list(self, common_list):
        print(common_list.val)
        node = common_list.next
        while node:
            print(node.val)
            node = node.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(6)

c = Solution()
lst = c.mergeTwoLists(l1, l2)
c.print_list(lst)
'''
1
1
2
3
4
6
'''