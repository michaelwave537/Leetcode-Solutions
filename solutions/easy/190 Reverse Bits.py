class Solution:
    def reverseBits(self, n: int) -> int:
        sol = 0
        power = 31
        for i in range(32):
            sol += (n%2) * (2**power)
            power -= 1
            n //= 2
        return (sol)