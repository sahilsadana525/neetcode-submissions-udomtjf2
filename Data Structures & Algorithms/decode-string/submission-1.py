class Solution:
    def decodeString(self, s: str) -> str:
        l = []
        for i in range(len(s)):
            b = ''
            if s[i] == ']':
                while l[-1] != '[':
                    b = l.pop() + b

                else:
                    l.pop()
                    num = ""
                    while l and l[-1].isdigit():
                         num = l.pop() + num
                    b = b*int(num)
                    l.append(b)
            else:
                l.append(s[i])
        if len(l) == 0:
            return b
        else:
            b = "" + "".join(l)
            return b