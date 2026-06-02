class MinStack:

    def __init__(self):
        self.l1 = []
        self.l2 = []

    def push(self, val: int) -> None:
        self.l1.append(val)
        if len(self.l2) == 0:
            self.l2.append(val)
        elif self.l2[-1] >= self.l1[-1]:
            self.l2.append(val)
        

    def pop(self) -> None:
        b = self.l1.pop()
        if b == self.l2[-1]:
            self.l2.pop()
        
        

    def top(self) -> int:
        return self.l1[-1]
        

    def getMin(self) -> int:
        return self.l2[-1]
        
