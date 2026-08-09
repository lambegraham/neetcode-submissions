# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        currNode = root

        while currNode:
            if p.val > currNode.val and q.val > currNode.val:
                currNode = currNode.right
            elif p.val < currNode.val and q.val < currNode.val:
                currNode = currNode.left
            else:
                return currNode