class Solution:
    def searchRange(self, nums, target: int):
        
        if target not in nums:
            return [-1, -1]

        if len(nums) == 1:
            return [0, 0]
        length = len(nums)
        start, end = 0, length - 1
        # middle = int(length/2)
        while end >= start:
            middle = int((end + start)/2)
            if target == nums[middle]:
                start_target = middle
                end_target = middle

                while start_target > 0 and nums[start_target - 1] == target:
                    start_target -= 1

                while end_target < length - 1 and nums[end_target + 1] == target:
                    end_target += 1

                return [start_target, end_target]
            # Update the length
            elif target > nums[middle]:
                start = int((start + end)/2) + 1
                continue
            elif target < nums[middle]:
                end = int((end + start)/2) - 1
                continue
