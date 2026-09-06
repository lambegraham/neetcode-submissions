# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head.next

        while fast and fast.next: #traverse to end
            slow = slow.next
            fast = fast.next.next
        #now we have slow = halfway point

        second = slow.next #create new from midway
        slow.next = None #cut the list

        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        #now we reversed the second list, join them back

        first = head
        second = prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
