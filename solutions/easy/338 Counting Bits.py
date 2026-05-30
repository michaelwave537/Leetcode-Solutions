class Solution:
    def countBits(self, n: int) -> List[int]:
        # sol = []
        # for i in range(n+1):
        #     index = i
        #     bits = []
        #     while index > 0:
        #         bits.append(index % 2)
        #         index //= 2
        #     sol.append(bits.count(1))
        # return sol

        dp = [0] * (n + 1)
        sub = 1

        for i in range(1, n + 1):
            if sub * 2 == i:
                sub = i
            
            dp[i] = dp[i - sub] + 1
        
        return dp