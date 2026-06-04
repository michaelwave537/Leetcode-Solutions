class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()

        if max(nums) != nums[len(nums)-2]:
            return False

        if max(nums) > 1:
            if nums.count(max(nums)) == len(nums):
                return False


        if max(nums) == len(nums)-1:
            for i in range(1, len(nums)):
                if i != nums[i-1]:
                    return False
            return True

        
        return False