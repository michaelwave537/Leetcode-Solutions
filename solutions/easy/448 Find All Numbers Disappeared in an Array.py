class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # sol = []
        # if len(nums) == 1:
        #     return sol
        
        # if min(nums) == max(nums):
        #     if max(nums) == 1:
        #         sol.append(max(nums)+1)
        #     else:
        #         sol.append(max(nums)-1)

        # else:
        #     for i in range(1, len(nums)+1):
        #         if i not in nums:
        #             sol.append(i)

        # return sol

        sol = list(set(range(1,len(nums)+1)) - set(nums))
        return sol