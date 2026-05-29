class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        count = 0
        copy = n
        while copy > 1:
            copy //= 3
            count += 1

        return 3 ** count == n
        
        # if n == 0: return False
        # count = 0
        # power = 0
        # while power < n:
        #     power = 3 ** count
        #     count += 1
        # return power == n