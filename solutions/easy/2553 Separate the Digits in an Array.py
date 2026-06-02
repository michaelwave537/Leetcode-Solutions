class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        # chars = []
        # for num in nums:
        #     for char in str(num):
        #         chars.append(int(char))

        # return chars

        chars = ""
        for num in nums:
            chars += str(num)

        char = list(map(int, chars))
        return char        