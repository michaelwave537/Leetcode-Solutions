class Solution:
    def minElement(self, nums: List[int]) -> int:
        sum_list = []
        for num in nums:
            sum = 0
            for char in str(num):
                sum += int(char)
            sum_list.append(sum)
        return min(sum_list)