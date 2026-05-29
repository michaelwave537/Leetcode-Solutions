class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        num = nums[0]
        for i in range(len(nums)):
            if nums[i] == num:
                count += 1
            else:
                num = nums[i]
            if count >= (len(nums) / 2):
                return nums[i]