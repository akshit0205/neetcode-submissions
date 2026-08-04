class Node:
    def __init__(self,key:int,val:int):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.Hash={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.Hash:
            pointer=self.Hash[key]                
            pointer.next.prev=pointer.prev
            pointer.prev.next=pointer.next
            pointer.next,pointer.prev=self.head.next,self.head
            self.head.next.prev=pointer
            self.head.next=pointer
            return pointer.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.Hash:
            old_node=self.Hash[key]
            old_node.val=value
            old_node.next.prev=old_node.prev
            old_node.prev.next=old_node.next
            old_node.next,old_node.prev=self.head.next,self.head
            self.head.next.prev=old_node
            self.head.next=old_node
            return
        if len(self.Hash)==self.capacity:
            x,k=self.tail.prev,self.tail.prev.key
            del self.Hash[k]
            x.prev.next=self.tail
            self.tail.prev=x.prev
            x=None
        x=self.head.next
        new_node=Node(key,value)
        x.prev=new_node
        self.head.next=new_node
        new_node.next,new_node.prev=x,self.head
        self.Hash[key]=new_node

