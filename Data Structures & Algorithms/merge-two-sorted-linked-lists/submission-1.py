# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = None
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list1.val == list2.val:
            list3 = ListNode(list1.val, ListNode(list2.val, self.mergeTwoLists(list1.next, list2.next)))
        if list1.val < list2.val:
            list3 = ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
        if list2.val < list1.val:
            list3 = ListNode(list2.val, self.mergeTwoLists(list1, list2.next))
        return list3