class MyHashMap:

    def __init__(self):
        self.l = []

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.l)):
            if self.l[i][0] == key:
                self.l[i][1] = value
                return
        self.l.append([key,value])
                
    def get(self, key: int) -> int:
        for i in range(len(self.l)):
            if self.l[i][0] == key:
                return self.l[i][1]
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.l)):
            if self.l[i][0] == key:
                del self.l[i]
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)