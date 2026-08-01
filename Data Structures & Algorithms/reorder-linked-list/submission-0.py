# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return
        slow,fast=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        curr,new,prev=slow.next,slow.next,None
        slow.next=None
        while curr :
            new=curr.next
            curr.next=prev
            prev=curr
            curr=new
        head2=prev
        while head and head2 :
            tmp1,tmp2=head.next,head2.next
            head.next=head2
            head2.next=tmp1
            head,head2=tmp1,tmp2