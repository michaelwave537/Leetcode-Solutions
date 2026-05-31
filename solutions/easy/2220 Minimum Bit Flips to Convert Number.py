class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # start_bits = []
        # goal_bits = []

        # while start > 0:
        #     start_bits.append(start % 2)
        #     start //= 2

        # while goal > 0:
        #     goal_bits.append(goal % 2)
        #     goal //= 2
        
        # while len(goal_bits) < len(start_bits):
        #     goal_bits.append(0)
        
        # while len(goal_bits) > len(start_bits):
        #     start_bits.append(0)

        
        # count = 0
        # for i in range(len(start_bits)):
        #     if start_bits[i] != goal_bits[i]:
        #         count += 1
        
        # return count
        
        xor_result = start ^ goal
        sol = 0
        
        while xor_result > 0:
            sol += xor_result & 1
            xor_result >>= 1
        
        return sol
