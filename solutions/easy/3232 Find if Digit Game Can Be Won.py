class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        singleSum = 0
        doubleSum = 0
        for i in range(len(nums)):
            if nums[i] < 10:
                singleSum += nums[i]
            else:
                doubleSum += nums[i]
        
        return (singleSum != doubleSum)