# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        end = head
        endOrder = []

        while end:
            endOrder.append(end.val)
            end = end.next
            
        startOrder = endOrder[:]
        endOrder.reverse()


        return startOrder == endOrder