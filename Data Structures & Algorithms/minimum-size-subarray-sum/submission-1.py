from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = len(nums)
        c =0
        for i in range(len(nums)):
            r = i
            s = 0
            while s<target and len(nums)>r:
                s = s + nums[r]
                r+=1
            if s >= target:
                l = min(l,len(nums[i:r]))
                c+=1
        if c == 0:
            return 0
        else:
            return l
        
            




