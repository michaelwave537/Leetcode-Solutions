class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                if maximum < count:
                    maximum = count
                count = 0
        
        return max(count, maximum)
