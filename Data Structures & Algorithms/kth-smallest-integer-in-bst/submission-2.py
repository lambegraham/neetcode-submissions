# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        curr = root

        while curr or stack:
            while curr: #go left until we cant
                stack.append(curr)
                curr = curr.left #keep going left
            curr = stack.pop() #pop left most
            k -= 1
            if k == 0: #we reached answer
                return curr.val
            curr = curr.right #go right until k == 0