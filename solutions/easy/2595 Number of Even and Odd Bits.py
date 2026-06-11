class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        sol = [0,0]
        bits = []

        while n > 0 :
            bits.append(n%2)
            n //= 2
        
        for index, bit in enumerate(bits):
            if bit == 1:
                if index % 2:
                    sol[1] += 1
                else:
                    sol[0] +=1

        return sol