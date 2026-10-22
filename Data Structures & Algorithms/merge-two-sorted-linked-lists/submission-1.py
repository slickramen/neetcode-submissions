# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            newTarg = -1

            if list1.val <= list2.val:
                newTarg = list1
                list1 = list1.next
            else:
                newTarg = list2
                list2 = list2.next
            
            curr.next = newTarg
            curr = curr.next

        if not list1:
            curr.next = list2
        elif not list2:
            curr.next = list1

        return dummy.next