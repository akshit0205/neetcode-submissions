# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists :return None
        Heap=[]
        for i,head in enumerate(lists):
            if head:heapq.heappush(Heap,(head.val,i,head))
        Head=ListNode(0,None)
        curr=Head
        pointer=None
        while Heap:
            value,i,pointer=heapq.heappop(Heap)
            curr.next=pointer
            curr=curr.next
            if pointer.next: heapq.heappush(Heap,(pointer.next.val,i,pointer.next))
        return Head.next
        