# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        list2 = slow.next
        slow.next = None
        list1 = head
        current = list2
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        list2 = prev
        while list2:
            next1 = list1.next
            next2 = list2.next
            list1.next = list2
            list2.next = next1
            list1 = next1
            list2 = next2