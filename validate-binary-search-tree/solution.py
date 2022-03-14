# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minimum = -2 ** 31
        maximum = 2 ** 31

        return self.validate(root, minimum, maximum)

    
    def validate(self, node, minimum, maximum):
        if node == None:
            return True

        if node.val < minimum or node.val > maximum:
            return False

        return self.validate(node.left, minimum, node.val - 1) and self.validate(node.right, node.val + 1, maximum)
    
