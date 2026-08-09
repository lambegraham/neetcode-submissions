# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val: #go left
            root.left = self.deleteNode(root.left, key)
        elif key > root.val: #go right
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            #find min from right subtree
            else:
                curr = root.right #set curr to root.right
                while curr.left: #go left
                    curr = curr.left
                root.val = curr.val #after going all the way left, replace root 
                root.right = self.deleteNode(root.right, root.val)
        return root
