# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #1. create minHeap, push (node.val, i, node)
        minHeap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, i, node)) #i is tie breaker
        #2. create dummy ListNode and cur
        dummy = ListNode(0)
        cur = dummy
        #3. while minHeap exists, pop _, i, node
        while minHeap:
            _, i, node = heapq.heappop(minHeap)
            #4. advance linkedList
            cur.next = node
            cur = cur.next
            #5. push (node.next.val, i, node.next) to heap
            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))
        #6. return dummy.next
        return dummy.next
