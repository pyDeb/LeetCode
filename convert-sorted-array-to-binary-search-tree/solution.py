# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        middle = int(len(nums)/2)

        root = TreeNode(val=nums[middle])
        if middle > 0:
            self.insert_to_tree(root, nums[:middle], nums[middle + 1:])

        return root


    def insert_to_tree(self, root, left_side, right_side):
        right_size = len(right_side)
        left_size = len(left_side)
        
        if left_size > 0:
            left_middle = int(left_size/2)
            left_root = TreeNode(val=left_side[left_middle])
            root.left = left_root
            if left_size > 1:
                self.insert_to_tree(left_root, left_side[:left_middle], left_side[left_middle + 1:])
        
        if right_size > 0:
            right_middle = int(right_size/2)
            right_root = TreeNode(val=right_side[right_middle])
            root.right = right_root
            if right_size > 1:
                self.insert_to_tree(right_root, right_side[:right_middle], right_side[right_middle + 1:])
        
        
