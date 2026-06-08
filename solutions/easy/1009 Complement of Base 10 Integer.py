class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        bits = []
        while n > 0:
            bits.append(n%2)
            n //= 2

        compliment = []
        for i in range(len(bits)):
            if bits[i] == 1:
                compliment.append(0)
            else:
                compliment.append(1)

        sol = 0
        power = 0

        for bit in compliment:
            if bit == 1:
                sol += bit * (2**power)
            power += 1

        return sol