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
            #now we know our total nodes
        
        removeNode = totalNodes - n #node we need to remove from end
        if removeNode == 0:
            return head.next

        curr = head 
        for i in range(totalNodes - 1):
            if (i + 1) == removeNode:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head
