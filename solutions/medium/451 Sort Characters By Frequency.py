class Solution:
    def frequencySort(self, s: str) -> str:
        chars = {char: s.count(char) for char in set(s)}
        sorted_chars = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
        sol = ""

        for char in sorted_chars:
            for i in range(sorted_chars.get(char)):
                sol += char
        return sol