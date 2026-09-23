# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count = {}
        current = head
        if current == None:
            return False
        while current.next not in count:
            if current.next == None:
                return False
            count[current] = 1
            current = current.next
        return True