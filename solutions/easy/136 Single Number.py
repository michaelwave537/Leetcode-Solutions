class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # numbers = []
        #
        # for i in range(len(nums)):
        #     if nums[i] not in numbers:
        #         numbers.append(nums[i])
        #     else:
        #         numbers.remove(nums[i])
        #
        # return numbers[0]

        # faster
        nums.sort()
        sol = 0
        prev = 0

        for i in range(len(nums)):
            if nums[i] != sol:
                prev = sol
                sol = nums[i]
            else:
                sol = prev
        return sol

            