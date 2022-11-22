class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct_nums = set()
        for num in nums:
            if num not in distinct_nums:
                distinct_nums.add(num)
            else:
                return True
        return False
      
