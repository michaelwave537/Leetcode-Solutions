class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1, num+1):
            number = str(i)
            sum = 0

            for char in number:
                sum += int(char)
            
            if not sum % 2:
                count += 1
        
        return count