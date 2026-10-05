# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse_linked(temp_head):
            if not temp_head or not temp_head.next:
                return temp_head
            reversed_list = reverse_linked(temp_head.next)
            temp_head.next.next = temp_head
            temp_head.next = None
            return reversed_list
        reverse_1 = reverse_linked(head)
        tail = reverse_1
        counter = 1
        while tail:
            if n == 1:
                return reverse_linked(reverse_1.next)
            elif counter == n - 1:
                temp = tail.next
                tail.next = temp.next
            else:
                tail = tail.next
            counter += 1
        return reverse_linked(reverse_1)