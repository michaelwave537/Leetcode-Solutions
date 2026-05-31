class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        # sum = 0
        # for index, num in enumerate(nums):
        #     i = index
        #     bits = []
        #     while i > 0:
        #         bits.append(i % 2)
        #         i //= 2
            
        #     if bits.count(1) == k:
        #         sum += num
        # return sum

        sum = 0
        for index, num in enumerate(nums):
            i = index
            count = 0
            while i > 0:
                if i % 2:
                    count += 1
                i //= 2
            
            if count == k:
                sum += num
        return sum