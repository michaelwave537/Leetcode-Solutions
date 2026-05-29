class Solution:
    def check(self, nums: List[int]) -> bool:
        
        # naive
        # index = 0
        # for i in range(len(nums)):
        #     if nums[i] == min(nums):
        #         index = i
        #         break

        # step = 0
        # for i in range(len(nums)):
        #     step = (index + i) % len(nums)
        #     if nums[step] == min(nums):
        #         continue
        #     # print(f'Step: {nums[step]}, Previous Step: {nums[step - 1]}')
        #     if nums[step] < nums[step-1]:
        #         return False


        # sort = nums.copy()
        # sort.sort()

        # if sort == nums:
        #     return True
        
        # if nums[-1] + 1 == nums[0] or nums[-1] == nums[0]:
        #     return True

        # for i in range(nums.count(min(nums))):
        #     step = (index + i) % len(nums)
        #     if nums[step] != min(nums):
        #         return False

        # return True

        N = len(nums)
        count = 1

        for i in range(1, 2 * N):
            if nums[(i - 1) % N] <= nums[i % N]:
                count += 1
            else:
                count = 1
            if count == N:
                return True
        return N == 1
        