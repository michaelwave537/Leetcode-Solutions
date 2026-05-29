class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # count = 0
        # copy = n
        # while copy > 1:
        #     copy //= 2
        #     count += 1

        # sol = 2 ** count
        # if sol == n:
        #     return True
        
        power = 1
        while power < n:
            power = power << 1
        return power == n

        # return False