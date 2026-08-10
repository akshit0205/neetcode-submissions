class Solution:
    def reverse(self, h, t):
        Stop=t.next
        prev, nex = None, h
        Tail = h
        while h != Stop:  
            nex = h.next
            h.next = prev
            prev = h
            h = nex
        return Tail, prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 1: 
            return head
            
        Dummy = ListNode(0, head)
        curr, pgt = head, Dummy
        count = 0
        
        while curr: 
            count += 1
            if count == k:
                nextgrp = curr.next
                Tail, pgt.next = self.reverse(head, curr)
                Tail.next = nextgrp 
                pgt = Tail
                head = curr = nextgrp
                count = 0
            else:
                curr = curr.next
                
        return Dummy.next