class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        
        # naive solution
        # nlist = []
        # for n in s:
        #     nlist.append(n)

        # prev_index = None
        # for index, current in enumerate(nlist):

        #     if index == prev_index:
        #         continue

        #     if current == "I":
        #         if index + 1 < len(nlist) and nlist[index + 1] == "V":
        #             sum = sum + 4
        #             index = index + 1
        #         elif index + 1 < len(nlist) and nlist[index + 1] == "X":
        #             sum = sum + 9
        #             index = index + 1
        #         else:
        #             sum = sum + 1

        #     elif current == "V":
        #         sum = sum + 5

        #     elif current == "X":
        #         if index + 1 < len(nlist) and nlist[index + 1] == "L":
        #             sum = sum + 40
        #             index = index + 1
        #         elif index + 1 < len(nlist) and nlist[index + 1] == "C":
        #             sum = sum + 90
        #             index = index + 1
        #         else:
        #             sum = sum + 10
                    
        #     elif current == "L":
        #         sum = sum + 50

        #     elif current == "C":
        #         if index + 1 < len(nlist) and nlist[index + 1] == "M":
        #             sum = sum + 900
        #             index = index + 1
        #         elif index + 1 < len(nlist) and nlist[index + 1] == "D":
        #             sum = sum + 400
        #             index = index + 1
        #         else:
        #             sum = sum + 100

        #     elif current == "D":
        #         sum = sum + 500

        #     elif current == "M":
        #         sum = sum + 1000

        #     prev_index = index
        #     print(f'index: {index}, sum: {sum}')

        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
            
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                sum -= roman[s[i]]
            else:
                sum += roman[s[i]]

        return sum