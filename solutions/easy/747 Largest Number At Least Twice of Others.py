class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        sol = 0

        for index, num in enumerate(nums):
            if max(nums) == num:
                sol = index

        nums.sort(reverse=True)
        if nums[0] < nums[1]*2:
            return -1
            
        return sol