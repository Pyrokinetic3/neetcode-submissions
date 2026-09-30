# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        def helper(head, temp_set):
            if not head:
                return False
            else:
                if head in temp_set:
                    return True
                else:
                    temp_set.add(head)
                    return helper(head.next, temp_set)
        return helper(head, set())