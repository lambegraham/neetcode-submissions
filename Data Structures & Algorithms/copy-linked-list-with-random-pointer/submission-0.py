"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        copies = {None: None}

        #first pass: just copy nodes
        curr = head
        while curr:
            copies[curr] = Node(curr.val) #copy just nodes first, not next or random
            curr = curr.next

        #second pass: copy next & random
        curr = head
        while curr:
            copy = copies[curr] #select node
            copy.next = copies[curr.next] #set next node
            copy.random = copies[curr.random] #set random node
            curr = curr.next #adv curr
        return copies[head]
        