class Solution:
    def reverse(self, x: int) -> int:
        num = ""
        y = str(x)

        if y[0] == "-":
            y = y[1::]
            num = "".join(["-", y[::-1]])
        else:
            num = y[::-1]

        if int(num) > (2**31) - 1 or int(num) < -(2**31):
            return(0)
            
        return(int(num))