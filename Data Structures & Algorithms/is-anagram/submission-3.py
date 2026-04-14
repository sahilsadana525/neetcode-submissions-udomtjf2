class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        for char in set(s):
            if s.count(char) != t.count(char):
                return False
        return True