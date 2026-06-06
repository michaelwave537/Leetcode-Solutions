class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) == 1:
            return num
        
        sol = 0
        while len(str(num)) != 1:
            sum = 0
            for char in str(num):
                sum += int(char)
            
            num = sum
            sol = sum

        return sol
