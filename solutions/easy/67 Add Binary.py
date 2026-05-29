class Solution:
    def addBinary(self, a: str, b: str) -> str:
        nums = []
        a_int = int(a)
        b_int = int(b)
        bin_sum = a_int + b_int
        

        for integer in str(bin_sum):
            nums.append(integer)
        
        output = ""
        carry = 0
        nums.reverse()

        for char in nums:
            if char == "2":
                if carry == 1:
                    output += "1"
                else:
                    output += "0"
                    carry = 1
            elif char == "1":
                if carry == 1:
                    output += "0"
                else:
                    output += "1"
            else:
                if carry == 1:
                    carry = 0
                    output += "1"
                else:
                    output += "0"

        if carry == 1:
            output += "1"

        output = output[::-1]
        return(output)
          