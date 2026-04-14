from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x = strs[0]
        c=0
        for i in range(1,len(strs)):
            while strs[i].find(x)!=0:
                x = x[0:len(x)-1]
                if not x:
                  return ""
        return x

        