class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c0 = 0 
        c1 = 0
        c2 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                c0+=1
            elif nums[i] == 1:
                c1+=1
            else:
                c2+=1
        for a in range(c0):
            nums[a] = 0
        for b in range(c0,c0+c1):
            nums[b] = 1
        for c in range(c0+c1,len(nums)):
            nums[c] = 2
            
        