class Solution:
    def hammingWeight(self, n: int) -> int:
        # power = 1
        # count = 0
        # while power <= n:
        #     power *= 2
        #     count += 1

        bits = []

        # for i in range(count+1):
        #     if n < power:
        #         if i != 0:
        #             bits.append(0)
        #     else:
        #         bits.append(1)
        #         n -= power
            
        #     power /= 2

        # return(bits.count(1))

        while n > 0:
            bits.append(n % 2)
            n //= 2
        
        return(bits.count(1))
        