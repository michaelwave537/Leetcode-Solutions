class Solution:
    def firstUniqChar(self, s: str) -> int:
        let = {char: s.count(char) for char in set(s)}

        for i, c in enumerate(s):
            if let[c] == 1:
                return i
        
        return -1
