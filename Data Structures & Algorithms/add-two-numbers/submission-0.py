# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 : return l2
        if not l2 : return l1
        x,y=l1,l2
        ans,value=ListNode(0),0
        carry=0
        curr=ans
        while x or y or carry:
            val1=x.val if x else 0
            val2=y.val if y else 0
            total=carry+val1+val2
            carry=total//10
            digit=total%10
            curr.next=ListNode(digit)
            curr=curr.next
            if x: x=x.next
            if y: y=y.next
        return ans.next