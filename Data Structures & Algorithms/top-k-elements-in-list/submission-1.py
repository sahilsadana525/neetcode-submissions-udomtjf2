from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1

        ans = sorted(d, key=d.get, reverse=True)

        return ans[:k]
