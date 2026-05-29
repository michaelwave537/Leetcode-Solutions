class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""

        # naive solution
        # while num > 0:
        #     print(num)
        #     if num >= 1000:
        #         num -= 1000
        #         roman += "M"
            
        #     elif num >= 500:
        #         if num >= 900:
        #             num -= 900
        #             roman += "CM"
        #         else:
        #             num -= 500
        #             roman += "D"
            
        #     elif num >= 100:
        #         if num >= 400:
        #             num -= 400
        #             roman += "CD"
        #         else:                
        #             num -= 100
        #             roman += ("C")
            
        #     elif num >= 50:
        #         if num >= 90:
        #             num -= 90
        #             roman += "XC"
        #         else:                
        #             num -= 50
        #             roman += ("L")

        #     elif num >= 10:
        #         if num >= 40:
        #             num -= 40
        #             roman += ("XL")
        #         else:
        #             num -= 10
        #             roman += ("X")

        #     elif num >= 5:
        #         if num >= 9:
        #             num -= 9
        #             roman += ("IX")
        #         else:                
        #             num -= 5
        #             roman += ("V")

        #     elif num >= 1:
        #         if num >= 4:
        #             num -= 4
        #             roman += ("IV")
        #         else:                
        #             num -= 1
        #             roman += ("I")
        
        symbols =  [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], 
                    ["XC", 90], ["C", 100], ["CD", 400],["D", 500],["CM", 900],["M", 1000]]

        for symbol, value in reversed(symbols):
            if num // value:
                count = num // value
                roman += (symbol * count)
                num = num % value
                
        return roman