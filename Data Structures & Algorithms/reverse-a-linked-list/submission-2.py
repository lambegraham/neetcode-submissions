# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            tmp = curr.next #save this for later
            curr.next = prev #set next one to None
            prev = curr #set the prev to be the current
            curr = tmp #set current to be the old next
        return prev