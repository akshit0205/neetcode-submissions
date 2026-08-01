# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head : return head
        dummy = ListNode(0, head)
        first = dummy
        second = dummy
        for _ in range(n):
            first=first.next
        while first.next:
            second=second.next
            first=first.next
        if second.next: second.next=second.next.next
        return dummy.next
