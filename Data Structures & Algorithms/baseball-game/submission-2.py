from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l=[]
        for i in range(len(operations)):
            if operations[i].isdigit() or operations[i].lstrip('-').isdigit(): 
                l.append(int(operations[i]))
                print(l)
            elif operations[i] == 'D':
                l.append(int(l[len(l)-1])*2)
            elif operations[i] == 'C':
                l.pop()
                print(l)
            else:
                l.append(int(l[len(l)-1])+int(l[len(l)-2]))
                print(l)
        return sum(l)