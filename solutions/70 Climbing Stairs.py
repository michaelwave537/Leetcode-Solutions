class Solution:
    def climbStairs(self, n: int) -> int:   

        # if n == 1:
        #     return 1
        # sol = 0

        # too slow
        # def climbing(n):
        #     # print(f'Number of steps left: {n}')
        #     nonlocal sol
        #     if n == 0:
        #         # print("Solution found")
        #         sol += 1
        #         return

        #     if n - 2 >= 0:
        #         # print("Step 2")
        #         climbing(n-2)

        #     if n - 1 >= 0:
        #         # print("Step 1")
        #         climbing(n-1)
        
        # climbing(n)
        # print(sol)

        # return sol

        memo = {}

        def climbing(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            if n in memo:
                return memo[n]

            memo[n] = climbing(n - 1) + climbing(n - 2)
            return memo[n]

        return climbing(n)