# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        x,y=head,head
        while x and x.next :
            x=x.next.next
            y=y.next
            if x is y: return True
        return False