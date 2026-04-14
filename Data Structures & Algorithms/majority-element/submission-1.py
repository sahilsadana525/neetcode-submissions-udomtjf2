class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)):
            if c<nums.count(nums[i]):
                c = nums.count(nums[i])
                s = nums[i]
        return s
        