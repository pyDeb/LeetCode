class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use a hasmap yo!
        length = len(nums)
        for num in nums:
            nums[(num - 1) % length] += length
        
        # return nums
        for i in range(length):
            if nums[i] / length > 2:
                return i + 1
        
