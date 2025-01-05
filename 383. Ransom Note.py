class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = list(magazine)
        ran = list(ransomNote)
        for i in ran:
            if i in mag:
                mag.remove(i)
            else:
                return False
        return True
