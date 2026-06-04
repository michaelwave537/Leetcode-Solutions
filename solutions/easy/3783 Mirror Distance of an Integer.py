class Solution:
    def mirrorDistance(self, n: int) -> int:
        reverse_n = str(n)[::-1]
        return(abs(n - int(reverse_n)))