class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ordered = []
        for height in heights:
            ordered.append(height)
        
        ordered.sort()

        count = 0
        for i in range(len(heights)):
            if ordered[i] != heights[i]:
                count += 1
        
        return count