# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = [] #[node.val, ]
        for i, node in enumerate(lists): 
            if node:
                heapq.heappush(minHeap, (node.val, i, node))
            
        dummy = ListNode(0)
        curr = dummy

        while minHeap:
            _, index, node = heapq.heappop(minHeap)

            if node:
                curr.next = node
                curr = curr.next

                if node.next:
                    heapq.heappush(minHeap, (node.next.val, index, node.next))
        return dummy.next
            