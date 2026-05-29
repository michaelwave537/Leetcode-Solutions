class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        last = f'{s[-1:]}'
        word = []
        for char in last.strip("[").strip("]").strip("'"):
            word.append(char)

        return (len(word))