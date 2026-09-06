# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1 #attach it to new linkedList
                list1 = list1.next #advance old list
            else:
                node.next = list2
                list2 = list2.next
            node = node.next #advance new list
        node.next = list1 or list2 #when out of both, attach all of remaining list
        return dummy.next
        