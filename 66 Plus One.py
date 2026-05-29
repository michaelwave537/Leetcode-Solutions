class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # if digits[-1] == 9:
        #     digits[-1] = 1
        #     new_list = [0]
        #     for num in digits:
        #         new_list.append(num)
        #     new_list.reverse()
        #     return (new_list)
        # else:
        #     digits[-1] = digits[-1] + 1
        # return digits

        num = ""
        for integer in digits:
            num += str(integer)
        num = int(num) + 1
        new_list = []
        for char in str(num):
            new_list.append(int(char))
        return (new_list)
