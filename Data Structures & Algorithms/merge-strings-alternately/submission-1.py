class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = list(word1)
        l2 = list(word2)
        l3 = []
        s=''
        if len(l1)<len(l2):
            for i in range(len(l1)):
                l3.append(l1[i])
                l3.append(l2[i])
            l3.extend(l2[i+1:])
        elif len(l1)>len(l2):
            for i in range(len(l2)):
                l3.append(l1[i])
                l3.append(l2[i])
            l3.extend(l1[i+1:])
        else:
            for i in range(len(l2)):
                l3.append(l1[i])
                l3.append(l2[i])
        s = s.join(l3)
        return s
