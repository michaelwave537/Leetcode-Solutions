class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        sol = []
        odd = []
        for num in nums:
            if num % 2 == 0:
                sol.append(num)
            else:
                odd.append(num)
        
        sol += odd
        return sol