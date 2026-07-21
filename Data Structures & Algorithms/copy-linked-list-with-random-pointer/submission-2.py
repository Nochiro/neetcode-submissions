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
        if not head:
            return None
        copies = {}
        curr = head
        while curr:
            copy = Node(curr.val)
            copies[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                copies[curr].next = copies[curr.next]
            else:
                copies[curr].next = None
            copies[curr].random = copies.get(curr.random)
            curr = curr.next
        return copies[head]            