# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head) #0, next
        groupPrev = dummy #node before group we reverse

        while True:
            curr = groupPrev.next
            counter = 0

            while curr and counter < k:
                curr = curr.next
                counter += 1
            
            if counter < k:
                break #fewer than k = remain unchanged

            groupNext = curr #first node AFTER group
            groupStart = groupPrev.next #tail after reverse - dummy.next -> start

            prev = groupNext #make new tail connect to next group
            curr = groupStart

            for _ in range(k): #reverse LL
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
        
            groupPrev.next = prev #connect preceding node to group head
            groupPrev = groupStart #new tail sites before the next group

        return dummy.next
            