class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range(0,len(nums)):
           for j in range(0,len(nums)):
            if nums[i]+nums[j] == target and i!=j:
                if i<j:
                    l.append(i)
                    l.append(j)
                else:
                    l.append(j)
                    l.append(i)
                return l
