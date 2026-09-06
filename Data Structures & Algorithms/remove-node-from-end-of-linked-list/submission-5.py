# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head 
        totalN = 0

        while curr:
            totalN += 1
            curr = curr.next
        
        removeN = totalN - n 
        if removeN == 0:
            return head.next
        
        curr = head
        for i in range(totalN - 1):
            if (i + 1) == removeN:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head