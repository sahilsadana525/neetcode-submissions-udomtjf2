from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = 1
        b = 0
        l = sorted(nums)
        print(l)
        for i in range(0,len(l)-1):
            if l[i+1] - l[i] == 1:
                a+=1
            elif l[i+1] == l[i]:
                continue
            else:
                if b < a:
                    b = a
                    a = 1
                else:
                   a = 1
        if b < a and len(l)!=0:
            return a
        else:
            return b