class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = {}
        for i,num in enumerate(numbers):
            complement = target - num
            if complement in mp:
                return [mp[complement]+1,i+1]
            mp[num] = i
        return [-1,1]

