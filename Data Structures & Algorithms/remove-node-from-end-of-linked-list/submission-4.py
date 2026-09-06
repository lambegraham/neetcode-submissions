# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        totalNodes = 0

        curr = head
        while curr:
            totalNodes += 1
            curr = curr.next
        
        removeNode = totalNodes - n #the index we want to remove
        curr = head

        if removeNode == 0:
            return head.next

        for i in range(totalNodes - 1):
            if (i + 1) == removeNode: #we are 1 before, remove next
                curr.next = curr.next.next
                break
            curr = curr.next
        
        return head