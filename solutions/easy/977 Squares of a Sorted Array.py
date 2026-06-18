class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sol = []
        for num in nums:
            sol.append(num**2)
        
        sol.sort()
        return sol