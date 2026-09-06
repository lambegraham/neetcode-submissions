# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        #[[1,2,4],[1,3,5],[3,6]]
        # heap: [(1,0,node)]
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, i, node))
        
        dummy = ListNode(0)
        curr = dummy

        while minHeap:
            _, i, node = heapq.heappop(minHeap) #o(logn) pop

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))

        return dummy.next



