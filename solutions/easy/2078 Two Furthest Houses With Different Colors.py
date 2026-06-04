class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # index = 0
        # for i in range(len(colors)):
        #     if colors[0] != colors[i]:
        #         index = i

        # farthest = 0
        # for i, house in enumerate(colors):
        #     if house != colors[-1]:
        #         farthest = abs(i - (len(colors)-1))
        #         break

        # return max(index, farthest)

        left, right = 0, 0
        for i, house in enumerate(colors):
            if colors[0] != house:
                left = max(left, i)
            if colors[-1] != house:
                right = max(right, len(colors)-1-i)
        
        return max(left, right)