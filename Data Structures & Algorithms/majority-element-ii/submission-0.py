from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = []
        for i in range(n):
            if nums[i] not in l:
                if nums.count(nums[i]) > n//3:
                    l.append(nums[i])
        return l
                

