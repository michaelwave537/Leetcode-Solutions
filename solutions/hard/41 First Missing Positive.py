class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # nums = list(set(nums))
        # nums.sort()
        # index = 1
        # for num in nums:
        #     if num < 1:
        #         continue
        #     if index != num:
        #         return index
        #     else:
        #         index += 1
         
        # return index

        # O(n) time and O(1) auxiliary space
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct = nums[i] - 1
                nums[i], nums[correct] = nums[correct], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1        