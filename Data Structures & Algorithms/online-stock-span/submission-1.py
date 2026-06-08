class StockSpanner:

    def __init__(self):
        self.l1 = []

    def next(self, price: int) -> int:
        self.l1.append(price)
        a = 0
        t = False
        l = len(self.l1)-1
        for i in range(len(self.l1)-1,-1,-1):
            a+=1
            if self.l1[l] < self.l1[i-1]:
                t = True
                break
        if t == False and a==1:
            return 1
        else:
            return a
            



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)