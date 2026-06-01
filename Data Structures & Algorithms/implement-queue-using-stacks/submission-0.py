class MyQueue:

    def __init__(self):
      self.l1 = []
      self.l2 = []  

    def push(self, x: int) -> None:
        self.l1.append(x)

    def pop(self) -> int:
        if len(self.l2)==0:
            for i in range(len(self.l1)):
                self.l2.append(self.l1.pop())
            return self.l2.pop()
        else:
            return self.l2.pop()


    def peek(self) -> int:
        if not self.l2:
            while self.l1:
                self.l2.append(self.l1.pop())

        return self.l2[-1]

    def empty(self) -> bool:
        if len(self.l2) == 0 and len(self.l1) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()