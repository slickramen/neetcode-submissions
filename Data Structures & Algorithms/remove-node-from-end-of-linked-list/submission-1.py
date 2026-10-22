# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head

        rev = []

        while curr:
            rev.append(curr)

            curr = curr.next

        idx = len(rev) - n
        if idx == 0:
            return head.next

        rev[idx - 1].next = rev[idx].next

        return head