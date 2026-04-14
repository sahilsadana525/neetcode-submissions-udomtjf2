from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = []

        if not strs:
            return [[""]]
        if len(strs) == 1:
            return [strs]

        for i in range(len(strs)):
            # Check if the element already exists in any previous group
            exists = False
            for k in l:
                if strs[i] in k:
                    exists = True
                    break
            if exists:
                continue    # skip this word, already grouped

            # Create a new group
            l1 = [strs[i]]

            # Compare strs[i] with remaining words
            for j in range(i + 1, len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    l1.append(strs[j])

            l.append(l1)

        return l

        