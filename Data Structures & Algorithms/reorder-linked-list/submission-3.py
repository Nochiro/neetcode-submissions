# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        first = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        curr = second
        while curr:
            nxt =  curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev
        while first and second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            if temp1:
                second.next = temp1
            first = temp1
            second = temp2
            


