class Solution:
    def smallestNumber(self, n: int) -> int:
        count = 0
        while n > 0:
            count += 1
            n //= 2

        sol = 1
        for i in range(count):
            sol = sol * 2
        sol -= 1
        return sol  
      