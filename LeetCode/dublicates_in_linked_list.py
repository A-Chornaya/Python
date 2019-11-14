# Remove Duplicates from Sorted List
'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        new_list = None
        new_list_head = new_list
        current = head
        nextt = current
        dubble_flag = False
        while current:
            nextt = nextt.next
            if nextt and current.val == nextt.val:
                dubble_flag = True
            else:
                if not dubble_flag:
                    if new_list is None:
                        new_list = ListNode(current.val)
                        new_list_head = new_list
                    else:
                        new_list_head.next = ListNode(current.val)
                        new_list_head = new_list_head.next
                current = nextt
                dubble_flag = False

        return new_list

    def print_list(self, head):
        while head:
            print(head.val)
            head = head.next


c = Solution()
examp = ListNode(1)
examp.next = ListNode(2)
examp.next.next = ListNode(3)
examp.next.next.next = ListNode(3)
examp.next.next.next.next = ListNode(4)
examp.next.next.next.next.next = ListNode(4)
examp.next.next.next.next.next.next = ListNode(5)
remove_dubble = c.deleteDuplicates(examp)
c.print_list(remove_dubble)
