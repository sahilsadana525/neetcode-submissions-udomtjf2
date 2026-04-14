class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''
        for i in range(len(s)):
            if s[i].isalnum():
                st = st + s[i]
        if st[:].lower() == st[::-1].lower():
            return True
        else:
            return False
                

        