class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = []
        for i in range(len(temperatures)):
            a = 0
            f = False
            for j in range(i+1,len(temperatures)):
                a+=1
                if temperatures[i] < temperatures[j]:
                    f = True
                    break
            if f:
                l.append(a)
            else:
                l.append(0)
        return l