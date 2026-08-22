"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = {}
        curr = head
        while curr:
            copy[curr] = Node(curr.val)
            curr = curr.next
        curr = head    
        while curr:
            if curr.next:
                copy[curr].next = copy[curr.next]
            else:
                copy[curr].next = None
            if curr.random:
                copy[curr].random = copy[curr.random]
            else:
                copy[curr].random = None
            curr = curr.next    
        if head:
            return copy[head]
        else:
            return None    