class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note = {char: ransomNote.count(char) for char in set(ransomNote)}
        mag = {char: magazine.count(char) for char in set(magazine)}

        if note == mag:
            return True
            
        count = 0
        for char in note:
            if char in mag:
                if note.get(char) <= mag.get(char):
                    count += 1

        if count == len(note):
            return True

        return False