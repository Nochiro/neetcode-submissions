# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        if not head or not head.next:
            return
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next    
        slow.next = None    
        prev = None
        curr = second
        while curr:
             next = curr.next
             curr.next = prev
             prev = curr
             curr = next
        list1 = head
        list2 = prev
        while list1 and list2:
            next1 = list1.next
            next2 = list2.next
            list1.next = list2
            if next1:
                list2.next = next1
            list1 = next1
            list2 = next2                         